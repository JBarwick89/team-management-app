from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import declarative_base

# TODO: hide this?
DATABASE_URL = "postgresql+asyncpg://team_management_app_user:yAJCIJ3SvtOqGxuFx1tGGR6RoPUXEQtt@dpg-d23thhvdiees73a1pvn0-a.oregon-postgres.render.com/team_management_app"

engine = create_async_engine(DATABASE_URL)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)
Base = declarative_base()
