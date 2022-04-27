import asyncio
from functools import partial
from typing import Callable

import aio_pika
from aio_pika import Message

from app.dependencies import get_settings
from app.models import AMQPMessage


class AMQPClient:

    async def init(self) -> None:
        '''
        Inititalize AMQP client.
        '''

        settings = get_settings()
        self.connection = await aio_pika.connect_robust(
            settings.RABBITMQ_BROKER_URL, loop=asyncio.get_event_loop()
        )

        # Creating channel
        self.channel = await self.connection.channel()
        await self.channel.set_qos(prefetch_count=1)

        return self

    async def event_store(self, exchange_name):
        '''
        Create an event-store. Client can send and consume events/messages from this event-store.

        exchange_name   -   Create an exchange to store events (event-store).
        '''

        self.exchange = await self.channel.declare_exchange(
            exchange_name,
            type='topic',
            durable=True
        )

    async def event_consumer(
        self, callback: Callable, event: str = '#', queue_name: str | None = None,
    ) -> None:
        '''
        Create an event consumer.

        callback    -   A function that will process the incoming message.
        event       -   Serves as a binding key or a type of event that occurred.
        queue_name  -   Create a queue to set of events from the Exchange (Optional).
                        If not specified it will still create a queue with a random name.
        '''

        queue = await self.channel.declare_queue(queue_name, auto_delete=True)
        await queue.bind(self.exchange, event)
        await queue.consume(partial(self._process_message, callback=callback))

    async def event_producer(
        self, exchange: str, binding_key: str, message: AMQPMessage
    ) -> None:
        '''
        Send event/message to a specific exchange with binding-key.

        If an existing queue is bound to the given binding-key, the message will be stored
        to that queue otherwise the message will be lost.

        NOTE: The binding_key is mandatory so we can explicitly route the message/event
            to the right queue.
        '''

        # Declare exchange
        exchange = await self.channel.declare_exchange(
            exchange,
            type='topic',
            durable=True
        )

        await exchange.publish(
            Message(
                body=str(message.dict()).encode(),
                content_type='application/json',
            ),
            routing_key=binding_key,
        )

    async def _process_message(self, message: aio_pika.IncomingMessage, callback: Callable) -> None:
        '''
        Process incoming message from a Queue. It will require a callback function to handle
        message content.
        '''
        async with message.process(ignore_processed=True):
            await message.ack()
            await callback(message.body)
