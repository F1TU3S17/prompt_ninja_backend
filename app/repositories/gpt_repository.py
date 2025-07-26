import json
import httpx
from app.core.config import settings

class GptRepository:
    def __init__(self):
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.api_key = settings.OPEN_ROUTER_API_KEY
        self.model ='deepseek/deepseek-r1'

    async def get_ui_schema(self, user_input: str, system_prompt: str) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                url=self.base_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    "model": self.model,
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
                ]})
                response.raise_for_status()
                data = response.json()
                return data
        except Exception as e:
            print(f"Error fetching UI schema: {e}")
            return None

    async def get_validation_prompt(self, prompt_data: dict, system_prompt: str) -> dict:
        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                url=self.base_url,
                headers={
                    'Content-Type': 'application/json',
                    'Authorization': f'Bearer {self.api_key}'
                },
                json={
                    "model": self.model,
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
                response.raise_for_status()
                data = response.json()
                return data
        except Exception as e:
            print(f"Error fetching UI schema: {e}")
            return None

    
