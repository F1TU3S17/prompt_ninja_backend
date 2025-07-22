import httpx
from app.core.config import settings

class SupabaseService:
    def __init__(self):
        self.supabase_anon_key = settings.SUPABASE_ANON_KEY
        self.supabase_url = settings.SUPABASE_URL
    
    async def save_prompt_template(self, prompt_template: dict, user_token: str):
        """
        Save the prompt template to Supabase.
        """
        json_data = {}
        json_data['json_data'] = prompt_template
        async with httpx.AsyncClient() as client:
            response = await client.post(
                url=f"{settings.SUPABASE_URL}/rest/v1/rpc/save_prompt_template",
                headers={
                    'Content-Type': 'application/json',
                    'apikey': self.supabase_anon_key,
                    'Authorization': f'Bearer {user_token}'
                },
                json=json_data
            )
            response.raise_for_status()
            return response.json()
            

    