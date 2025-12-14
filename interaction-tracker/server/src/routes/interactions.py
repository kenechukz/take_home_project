from fastapi import APIRouter
from main import app
from schemas import InteractionCreatePayload


router = APIRouter(prefix="/interactions", tags=["interactions"])



@router.post("/")
def create_interaction(request_body: InteractionCreatePayload):
    interaction = request_body.model_dump()


        