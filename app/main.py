from fastapi import FastAPI
from routes import auth, equipments, maintenances, components

app = FastAPI()

app.include_router(auth.auth_router, prefix="/auth")
app.include_router(equipments.router, prefix="/equipments")
app.include_router(maintenances.router, prefix="/maintenances")
app.include_router(components.router, prefix="/components")