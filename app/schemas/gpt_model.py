from pydantic import BaseModel, Field
from typing import Literal


class GptModel(BaseModel):
    """
    Модель для представления GPT провайдера и его конфигурации.
    """
    name: str = Field(..., description="Название модели")
    base_url: str = Field(..., description="Базовый URL API эндпоинта")
    api_key: str = Field(..., description="API ключ для авторизации")
    provider: Literal["mistral", "openrouter"] = Field(..., description="Провайдер модели")
    
    class Config:
        # Пример конфигурации модели
        schema_extra = {
            "example": {
                "name": "open-mistral-nemo",
                "base_url": "https://api.mistral.ai/v1/chat/completions",
                "api_key": "your-api-key-here",
                "provider": "mistral"
            }
        }
