from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.routers import templates
from app.routers import router_helthcheck


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")


app.include_router(templates.router, prefix="/page", tags=["templates"])
app.include_router(router_helthcheck.router, prefix="/api/helthcheck", tags=["helthcheck"])
