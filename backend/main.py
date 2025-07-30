from http.client import HTTPException
import uvicorn
from uuid import UUID
from fastapi import FastAPI, Depends, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Sequence
from team_management_app.schemas import Squad, SquadsResponse, SquadCreate
from team_management_app.database import AsyncSessionLocal
import team_management_app.crud as crud

app = FastAPI()

origins: List[str] = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


async def get_db() -> AsyncSession:
    """Dependency to get a DB session for each request."""
    async with AsyncSessionLocal() as session:
        yield session


# --- API Endpoints ---
@app.get("/squads", response_model=SquadsResponse)
async def get_all_squads(db: AsyncSession = Depends(get_db)):
    """Fetch all squads."""
    all_squads: Sequence[Squad] = await crud.get_squads(db)

    return SquadsResponse(squads=all_squads)


@app.post("/squads", response_model=Squad, status_code=201)
async def add_squad(squad: SquadCreate, db: AsyncSession = Depends(get_db)):
    """Create a new squad."""
    return await crud.create_squad(db=db, squad=squad)


@app.put("/squads/{squad_id}", response_model=Squad)
async def update_squad_endpoint(
    squad_id: UUID, squad: Squad, db: AsyncSession = Depends(get_db)
):
    """Update a squad by its ID."""
    updated_squad = await crud.update_squad(db, squad_id, squad)
    if updated_squad is None:
        raise HTTPException(status_code=404, detail="Squad not found")
    return updated_squad


@app.delete("/squads/{squad_id}", status_code=204)
async def delete_squad_endpoint(squad_id: UUID, db: AsyncSession = Depends(get_db)):
    """Delete a squad by its ID."""
    deleted_squad = await crud.delete_squad(db, squad_id)
    if deleted_squad is None:
        raise HTTPException(status_code=404, detail="Squad not found")
    return Response(status_code=204)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
