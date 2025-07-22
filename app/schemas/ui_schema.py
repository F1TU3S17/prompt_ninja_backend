from typing import List, Literal, Optional

from pydantic import BaseModel

class UISchemaRequest(BaseModel):
    prompt_template: str

class UIField(BaseModel):
    id: str
    type: Literal["text_input", "textarea", "dropdown"]
    label: str
    placeholder: Optional[str] = None
    options: Optional[List[str]] = None

class UISchemaResponse(BaseModel):
    status: Literal["success", "error"]
    message: Optional[str] = None
    ui_schema: Optional[List[UIField]] = None