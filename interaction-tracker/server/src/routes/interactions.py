from fastapi import APIRouter
from src.schemas import InteractionCreatePayload
from src.services.interactions import create_interaction 


router = APIRouter(prefix="/interactions", tags=["interactions"])



@router.post("/", status_code=201)
def create_interaction(request_body: InteractionCreatePayload):
    interaction = request_body.model_dump()

    return create_interaction(interaction)




        