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


async def retrieve_interaction(user_id: Optional[str], event_type:Optional[EventType]):

    where = {}

    if user_id:
        where["user_id"] = user_id

    if event_type:
        where["event_type"] = event_type.value



    return await db.interaction.find_many(where=where)


async def interaction_summary_statistics_service():

    count = await db.interaction.count()

    count_by_event_type = await db.interaction.group_by(by=["event_type"], count=True)

    count_by_user =  await db.interaction.group_by(by=["user_id"], count=True, 
        order={
            'event_type': 'asc',
    })
    
    data = {"count_by_event_type": []}

    for event in count_by_event_type:

        data["count_by_event_type"].append({event['event_type']: event['_count']}) 

    count_by_event_type = data
    

    data = {"count_by_user": []}
    for user in count_by_user:

        data["count_by_user"].append({user['user_id']: user['_count']}) 

    count_by_user = data

    #most_active_user =



    return 