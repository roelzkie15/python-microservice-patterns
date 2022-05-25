

from fastapi import Depends, FastAPI, Request
from strawberry.fastapi import GraphQLRouter

from app.amqp_client import AMQPClient
from app.db import Session
from app.schema import schema
from app.services import create_billing_request_from_event, set_billing_request_status_from_event

app = FastAPI()


@app.on_event('startup')
async def startup():
    amqp_client: AMQPClient = await AMQPClient().init()

    await amqp_client.event_consumer(create_billing_request_from_event, 'BOOKING_TX_EVENT_STORE', 'booking.created', 'booking_events')
    await amqp_client.event_consumer(set_billing_request_status_from_event, 'BOOKING_TX_EVENT_STORE', 'parking.unavailable')

    app.state.amqp_client = amqp_client


@app.on_event('shutdown')
async def shutdown():
    await app.state.amqp_client.connection.close()


@app.get('/health')
async def root():
    return {'message': 'Billing server is running'}


@app.middleware('http')
async def add_session_in_app_state(request: Request, call_next):
    with Session() as session:
        request.app.state.session = session
        response = await call_next(request)

    return response


graphql_app = GraphQLRouter(schema)
app.include_router(graphql_app, prefix='/graphql')
