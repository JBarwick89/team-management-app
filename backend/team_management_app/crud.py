from sqlalchemy import Result
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import joinedload, subqueryload
from uuid import UUID
from typing import Tuple, Sequence
from .models import Squad as SquadModel, TeamMember as TeamMemberModel
from .schemas import Squad as SquadSchema, SquadCreate, TeamMemberCreate


async def get_squads(db: AsyncSession) -> Sequence[SquadSchema]:
    result: Result[Tuple[SquadModel]] = await db.execute(
        select(SquadModel).options(subqueryload(SquadModel.members))
    )
    return result.scalars().all()


async def create_squad(db: AsyncSession, squad: SquadCreate) -> SquadCreate:
    db_members: list[TeamMemberCreate] = [
        TeamMemberModel(
            name=m.name,
            role=m.role,
            allocation=m.allocation,
        )
        for m in squad.members
    ]

    db_squad = SquadModel(
        name=squad.name,
        description=squad.description,
        members=db_members,
    )

    db.add(db_squad)
    await db.commit()
    await db.refresh(db_squad)
    return db_squad


async def update_squad(
    db: AsyncSession, squad_id: UUID, squad_data: SquadSchema
) -> SquadSchema | None:
    squadToUpdate: Result[Tuple[SquadModel]] = await db.execute(
        select(SquadModel)
        .where(SquadModel.id == squad_id)
        .options(joinedload(SquadModel.members))
    )
    db_squad: SquadModel | None = squadToUpdate.scalars().first()

    if db_squad:
        db_squad.name = squad_data.name
        db_squad.description = squad_data.description
        existing_member_ids = {member.id for member in db_squad.members}
        updated_members = []

        for m in squad_data.members:
            if m.id in existing_member_ids:
                # Update existing member
                member = next(
                    member for member in db_squad.members if member.id == m.id
                )
                member.name = m.name
                member.role = m.role
                member.allocation = m.allocation
            else:
                # Add new member
                new_member = TeamMemberModel(
                    id=m.id,
                    name=m.name,
                    role=m.role,
                    allocation=m.allocation,
                    squad_id=db_squad.id,
                )
                updated_members.append(new_member)

        # Remove members not in the updated data
        db_squad.members = [
            member
            for member in db_squad.members
            if member.id in {m.id for m in squad_data.members}
        ] + updated_members

        await db.commit()
        await db.refresh(db_squad)

    return db_squad


async def delete_squad(db: AsyncSession, squad_id: UUID) -> SquadModel | None:
    result: Result[Tuple[SquadModel]] = await db.execute(
        select(SquadModel)
        .where(SquadModel.id == squad_id)
        .options(joinedload(SquadModel.members))
    )
    db_squad: SquadModel | None = result.scalars().first()

    if db_squad:
        await db.delete(db_squad)
        await db.commit()

    return db_squad
