from pydantic import BaseModel, ConfigDict
from typing import List, Sequence
from uuid import UUID


# Base properties shared across create/update operations
class SquadCreate(BaseModel):
    name: str
    description: str
    members: List["TeamMemberCreate"] = []

    model_config = ConfigDict(from_attributes=True)


# Properties to receive via API on creation
# class SquadCreate(SquadBase):
#     pass


# # Properties to receive via API on update
# class SquadUpdate(SquadBase):
#     name: str
#     description: str


# Properties to return to client
class Squad(SquadCreate):
    id: UUID
    name: str
    description: str
    members: List["TeamMember"] = []

    model_config = ConfigDict(from_attributes=True)


# A wrapper for returning a list of squads
class SquadsResponse(BaseModel):
    squads: Sequence[Squad]


# Base properties shared across create/update operations
class TeamMemberCreate(BaseModel):
    name: str
    role: str
    allocation: float


class TeamMember(TeamMemberCreate):
    id: UUID
    squad_id: UUID
    name: str
    role: str
    allocation: float

    model_config = ConfigDict(from_attributes=True)
