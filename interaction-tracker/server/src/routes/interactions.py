from fastapi import APIRouter
from src.schemas import InteractionCreatePayload
from src.services.interactions import create_interaction as create_interaction_service


router = APIRouter(prefix="/interactions", tags=["interactions"])



@router.post("/", status_code=201)
async def create_interaction(request_body: InteractionCreatePayload):
    interaction = request_body.model_dump(exclude_none=True)
    created = await create_interaction_service(interaction)
    return created




        