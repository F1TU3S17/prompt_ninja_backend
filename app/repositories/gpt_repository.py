import json
import httpx

class GptRepository:
    def __init__(self):
        self.base_url = 'https://openrouter.ai/api/v1/chat/completions'
        self.api_key = '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'
        self.model ='deepseek/deepseek-r1'

    async def get_ui_schema(self, user_input: str, system_prompt: str):
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

    
