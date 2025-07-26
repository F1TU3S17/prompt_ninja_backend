from fastapi import APIRouter
from app.services.gpt_service import GptService

moderation_router= APIRouter(
    prefix="/moderation",
    tags=["Moderation"],    
)

@moderation_router.post("/validate-prompt-data")
async def validate_prompt_data(prompt_data: dict):
    gpt_service = GptService()
    result = await gpt_service.fetch_validation_prompt_data(prompt_data)
    return result