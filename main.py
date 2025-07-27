from fastapi import FastAPI
from app.api.v1.endpoints.ui_schema import router as ui_schema_router
from app.api.v1.endpoints.moderation import moderation_router

app = FastAPI(
    title='Prompt-ninja AI API', 
    version='1.0.0',
    description='API для создания UI схем и модерации контента с использованием AI'
)

# Health check endpoint
@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "prompt-ninja-api"}

app.include_router(
    router=ui_schema_router,
    prefix='/api/v1',
    tags=['UI Schema'],
)

app.include_router(
    router=moderation_router,
    prefix='/api/v1',
    tags=['Moderation'],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)