import uuid
from sqlalchemy import String, Float, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, Mapped, mapped_column
from .database import Base
from typing import List


class Squad(Base):
    __tablename__: str = "squads"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4()
    )
    name: Mapped[str] = mapped_column(String, index=True, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    members: Mapped[List["TeamMember"]] = relationship(
        "TeamMember", back_populates="squad", lazy="joined"
    )


class TeamMember(Base):
    __tablename__: str = "team_members"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), primary_key=True, default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(String, nullable=False)
    role: Mapped[str] = mapped_column(String, nullable=False)
    allocation: Mapped[float] = mapped_column(Float, nullable=False)
    squad_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True), ForeignKey("squads.id")
    )

    squad: Mapped[Squad] = relationship(
        "Squad", back_populates="members", lazy="joined"
    )
