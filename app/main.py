from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.api import auth, sites, templates, webhooks

app = FastAPI(
    title="ATProto Landing Builder",
    description="Create personalized landing pages using ATProto data",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
app.include_router(sites.router, prefix="/api/sites", tags=["sites"])
app.include_router(templates.router, prefix="/api/templates", tags=["templates"])
app.include_router(webhooks.router, prefix="/api/webhooks", tags=["webhooks"])

@app.get("/")
async def root():
    return {"message": "ATProto Landing Builder API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}