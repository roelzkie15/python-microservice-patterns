from uuid import UUID, uuid4

from sqlmodel import Field, SQLModel


class Booking(SQLModel, table=True):
    uuid: UUID = Field(default=str(uuid4()), primary_key=True)
    name: str
    status: str = Field(default='created')
