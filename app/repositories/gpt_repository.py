from app.core.logger import Logger
import httpx
from app.core.config import settings
from app.schemas.gpt_model import GptModel


class GptRepository:
    def __init__(self):
        self.models = [ 
            GptModel(
                name='open-mistral-nemo', 
                base_url='https://api.mistral.ai/v1/chat/completions', 
                api_key=settings.MISTRAL_API_KEY,
                provider='mistral'
            ),
            GptModel(
                name='mistral-small-2501', 
                base_url='https://api.mistral.ai/v1/chat/completions', 
                api_key=settings.MISTRAL_API_KEY,
                provider='mistral'
            ),
            GptModel(
                name='deepseek/deepseek-r1', 
                base_url='https://openrouter.ai/api/v1/chat/completions', 
                api_key=settings.OPEN_ROUTER_API_KEY,
                provider='openrouter'
            ), 
            GptModel(
                name='deepseek/deepseek-r1:free', 
                base_url='https://openrouter.ai/api/v1/chat/completions', 
                api_key=settings.OPEN_ROUTER_API_KEY,
                provider='openrouter'
            ),
        ]
        self.logger = Logger('GptRepository')
    async def get_ui_schema(self, user_input: str, system_prompt: str) -> dict:
        for model in self.models:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=model.base_url,
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {model.api_key}'
                    },
                    json={
                        "model": model.name,
                        "temperature": 1,
                        "messages": [
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": user_input
                            }
                        ]
                    }
                )
                if response.status_code != 200:
                    self.logger.error(f"Failed to fetch validation prompt with model {model}: {response.status_code} - {response.text}")
                    continue
                data = response.json()
                return data
        raise Exception(f"Failed to fetch UI schema with model {model}: {response.status_code} - {response.text}")

    async def get_validation_prompt(self, prompt_data: dict, system_prompt: str) -> dict:
        for model in self.models:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                url=model.base_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {model.api_key}'
                },
                json={
                    "model": model.name,
                    "temperature": 1,
                    "messages": [
                        {
                        "role": "system",
                        "content": system_prompt
                        },
                        {
                        "role": "user",
                        "content": str(prompt_data)
                        }
                ]})
                if response.status_code != 200:
                    self.logger.error(f"Failed to fetch validation prompt with model {model}: {response.status_code} - {response.text}")
                    continue
                data = response.json()
                return data
        raise Exception(f"Failed to fetch validation prompt: {response.status_code} - {response.text}")

    
