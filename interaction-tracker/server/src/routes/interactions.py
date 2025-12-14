from fastapi import APIRouter
from src.schemas import InteractionCreatePayload
from src.services.interactions import create_interaction 


router = APIRouter(prefix="/interactions", tags=["interactions"])



@router.post("/")
def create_interaction(request_body: InteractionCreatePayload):
    interaction = request_body.model_dump()




        