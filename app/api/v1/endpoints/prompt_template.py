from http.client import HTTPException
from typing import Annotated
from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.schemas.prompt_template import PromptTemplate, PromptTemplateResponse
from app.services.supabase_service import SupabaseService

security = HTTPBearer()
router = APIRouter(prefix="/prompt-template", tags=["Prompt Template"])

@router.post("/save", response_model=PromptTemplateResponse, summary="Save Prompt Template to Supabase")
async def save_prompt_template(
    prompt_template: PromptTemplate,
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    user_token = credentials.credentials
    response = await SupabaseService().save_prompt_template(prompt_template.model_dump(), user_token=user_token)
    if response['status'] != 'success':
        raise HTTPException(status_code=500, detail="Failed to save prompt template")
    return PromptTemplateResponse(**response)