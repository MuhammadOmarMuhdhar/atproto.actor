from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates

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
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

frontend_templates = Jinja2Templates(directory="frontend")

app.include_router(auth.router, prefix="/api/auth", tags=["authentication"])
# app.include_router(sites.router, prefix="/api/sites", tags=["sites"])
# app.include_router(templates.router, prefix="/api/templates", tags=["templates"])  
# app.include_router(webhooks.router, prefix="/api/webhooks", tags=["webhooks"])

@app.get("/")
async def homepage(request: Request):
    return frontend_templates.TemplateResponse("home/index.html", {"request": request})

@app.get("/login")
async def login_page(request: Request):
    return frontend_templates.TemplateResponse("login/index.html", {"request": request})

@app.get("/dashboard")
async def dashboard_page(request: Request):
    return frontend_templates.TemplateResponse("dashboard/index.html", {"request": request})

@app.get("/pricing")
async def pricing_page(request: Request):
    return frontend_templates.TemplateResponse("pricing/index.html", {"request": request})

@app.get("/help")
async def help_page(request: Request):
    return frontend_templates.TemplateResponse("help/index.html", {"request": request})

@app.get("/health")
async def health_check():
    return {"status": "healthy"}