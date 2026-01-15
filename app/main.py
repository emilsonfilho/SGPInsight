from fastapi import FastAPI
from routes import auth, equipments, maintenances, components, alerts, departments, roles, dashboard

app = FastAPI()

app.include_router(auth.auth_router, prefix="/auth")
app.include_router(equipments.router, prefix="/equipments")
app.include_router(maintenances.router, prefix="/maintenances")
app.include_router(components.router, prefix="/components")
app.include_router(alerts.router, prefix="/alerts")
app.include_router(departments.router, prefix="/departments")
app.include_router(roles.router, prefix="/roles")
app.include_router(dashboard.router, prefix="/dashboard")