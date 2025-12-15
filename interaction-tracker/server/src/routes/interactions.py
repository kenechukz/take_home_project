from fastapi import APIRouter, Query
from typing import Optional
from src.schemas import InteractionCreatePayload, EventType
from src.services.interactions import create_interaction as create_interaction_service
from src.services.interactions import retrieve_interaction as retrieve_interaction_service


router = APIRouter(prefix="/interactions", tags=["interactions"])



@router.post("/", status_code=201)
async def create_interaction(request_body: InteractionCreatePayload):
    interaction = request_body.model_dump(exclude_none=True)
    created = await create_interaction_service(interaction)
    return created


@router.get("/", status_code=200)
async def retrieve_interaction(
    user_id: Optional[str] = Query(None),
    event_type: Optional[EventType] = Query(None)):


    interactions = await retrieve_interaction_service(
        user_id=user_id,
        event_type=event_type,
    )
    return interactions




        