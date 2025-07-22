from fastapi import FastAPI
from app.api.v1.endpoints.ui_schema import router as ui_schema_router
from app.api.v1.endpoints.prompt_template import router as prompt_template_router
app = FastAPI(title='Prompt-ninja AI API', version='1.0.0',)

app.include_router(
    router=ui_schema_router,
    prefix='/api/v1',
    tags=['UI Schema'],
)

app.include_router(
    router=prompt_template_router,
    prefix='/api/v1',
    tags=['Prompt Template'],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)