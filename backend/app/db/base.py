from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


# Import models so SQLAlchemy knows about them
from app.db.models import *  # noqa: E402,F403