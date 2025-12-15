from prisma import Json
from src.db import db
from src.schemas import EventType
from typing import Optional


async def create_interaction(interaction: dict):
    metadata = interaction.get('metadata')
    metadata_value = Json(metadata) if metadata is not None else None
    return await db.interaction.create(
        data={
            'user_id': interaction['user_id'],
            'event_type': interaction['event_type'],
            'metadata': metadata_value,
        }
    )


async def retrieve_interaction(user_id: Optional[str], event_type:Optional[EventType]):

    where = {}

    if user_id:
        where["user_id"] = user_id

    if event_type:
        where["event_type"] = event_type.value



    return await db.interaction.find_many(where=where)
