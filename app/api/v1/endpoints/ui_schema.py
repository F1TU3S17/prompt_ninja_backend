from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.gpt_service import GptService
from app.schemas.ui_schema import UISchemaRequest, UISchemaResponse

router = APIRouter(prefix="/ui-schema", tags=["UI Schema"])


@router.post("/generate", response_model=UISchemaResponse, summary="Generate UI Schema from User Input Template")
async def generate_ui_schema(request: UISchemaRequest):
    gpt_service = GptService()
    ui_schema_response = await gpt_service.fetch_ui_schema(request.prompt_template)
    
    if not ui_schema_response:
        raise HTTPException(status_code=500, detail="Failed to generate UI schema")
    
    return ui_schema_response


