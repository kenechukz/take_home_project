from prisma import Json
from src.db import db


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
