from pydantic_settings import BaseSettings
class Settings(BaseSettings): 
    OPEN_ROUTER_API_KEY: str
    MISTRAL_API_KEY: str
    class Config:
        env_file = ".env"

settings = Settings()