from typing import List

from pydantic import BaseModel

from app.schemas.ui_schema import UIField


class PromptTemplate(BaseModel):
    name: str
    description: str
    template_text: str
    ui_schema: List[UIField]
    ai_tool_id: str
    category_id: str
    author_user_id: str
    prompt_language_id: str

class PromptTemplateResponse(BaseModel):
    status: str