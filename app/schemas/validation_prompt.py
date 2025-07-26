from pydantic import BaseModel


class ValidationPromptResponse(BaseModel):
    is_valid: bool
    message: str | None = None
   