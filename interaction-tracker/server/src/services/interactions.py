from prisma import Json
from src.db import db
from src.schemas import EventType
from typing import Optional, List, Dict, Any


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


def format_group_count_data(group_count: List[Dict[str, Any]], group_name: str):
    data = []
    for item in group_count:
        data.append({group_name: item.get(group_name),  "count": item.get('_count', {}).get('_all', 0)}) 

    return data


"""

What group by data looks like from documentation:
results = await db.profile.group_by(['country'], count=True)
# [
#   {'country': 'Denmark', '_count': {'_all': 20}},
#   {'country': 'Scotland', '_count': {'_all': 1}},
# ]

"""

async def interaction_summary_statistics_service():

    count = await db.interaction.count()

    count_by_event_type = await db.interaction.group_by(by=["event_type"], count=True)

    count_by_user =  await db.interaction.group_by(by=["user_id"], count=True, 
        order={
            "_count": {
                "user_id": "asc",  # Use the field name, not _all
        }
    })
    
    
    count_by_event_type = format_group_count_data(count_by_event_type, "event_type")
    
    count_by_user = format_group_count_data(count_by_user, "user_id")

    most_active_user = count_by_user[-1] if count_by_user else None

    return {
            "count": count,
            "count_by_event_type": count_by_event_type,
            "count_by_user": count_by_user,
            "most_active_user": most_active_user,
    }