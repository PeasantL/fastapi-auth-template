from fastapi import FastAPI

from . import routers


app = FastAPI()

app.include_router(routers.router_auth)
app.include_router(routers.router_user)
app.include_router(routers.router_item)