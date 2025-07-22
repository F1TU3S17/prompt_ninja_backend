from pydantic_settings import BaseSettings
class Settings(BaseSettings): 
    SUPABASE_ANON_KEY: str
    OPEN_ROUTER_API_KEY: str
    SUPABASE_URL: str
    class Config:
        env_file = ".env"

settings = Settings()