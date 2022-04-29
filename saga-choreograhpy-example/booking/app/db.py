import fire
from sqlmodel import SQLModel, create_engine

from app import models
from app.dependencies import get_settings

settings = get_settings()
engine = create_engine(settings.DB_URL, echo=True)


class BookingEngine:
    def create_db_and_tables(self):
        SQLModel.metadata.create_all(engine)


if __name__ == '__main__':
    fire.Fire(BookingEngine)
