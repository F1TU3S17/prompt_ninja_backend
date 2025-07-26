from app.core.logger import Logger
import httpx
from app.core.config import settings

class GptRepository:
    def __init__(self):
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.api_key = settings.OPEN_ROUTER_API_KEY
        self.models = ['deepseek/deepseek-r1', 'deepseek/deepseek-r1:free']

    async def get_ui_schema(self, user_input: str, system_prompt: str) -> dict:
        for model in self.models:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    url=self.base_url,
                    headers={
                        'Content-Type': 'application/json',
                        'Authorization': f'Bearer {self.api_key}'
                    },
                    json={
                        "model": model,
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
                    continue
                data = response.json()
                return data
        raise Exception(f"Failed to fetch UI schema with model {model}: {response.status_code} - {response.text}")

    async def get_validation_prompt(self, prompt_data: dict, system_prompt: str) -> dict:
        for model in self.models:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                url=self.base_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    "model": model,
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
                    Logger('Gpt repository').error(f"Failed to fetch validation prompt with model {model}: {response.status_code} - {response.text}")
                    continue
                data = response.json()
                return data
        raise Exception(f"Failed to fetch validation prompt: {response.status_code} - {response.text}")

    
