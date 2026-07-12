from datetime import datetime
from uuid import uuid4

from sqlalchemy.ext.mutable import MutableDict

from sqlalchemy import (
    DateTime,
    String,
    JSON,
    Integer,
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
)

from app.db.base import Base


class Project(Base):

    __tablename__ = "projects"


    id: Mapped[str] = mapped_column(
        String,
        primary_key=True,
        default=lambda: str(uuid4()),
    )


    name: Mapped[str] = mapped_column(
        String(200),
        nullable=False,
    )


    idea: Mapped[str] = mapped_column(
        String,
        nullable=False,
    )


    status: Mapped[str] = mapped_column(
        String(50),
        default="draft",
    )

    current_agent = mapped_column(
        String,
        nullable=True,
    )

    progress = mapped_column(
        Integer,
        default=0,
        nullable=False,
    )

    error_message = mapped_column(
        String,
        nullable=True,
    )

    history: Mapped[dict] = mapped_column(
        MutableDict.as_mutable(JSON),
        nullable=False,
        default=lambda: {"events": []},
    )


    ceo_analysis: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    technical_architecture: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    prd: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    design: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    marketing: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    investment: Mapped[dict | None] = mapped_column(
        JSON,
        nullable=True,
    )


    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
    )


    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
    )

    