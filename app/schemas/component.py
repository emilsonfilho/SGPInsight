from .base import Base
from datetime import datetime

class ComponentBase(Base):
    component_id: str
    equipment_id: str

class ComponentInstall(ComponentBase):
    observations: str

class ComponentRemove(ComponentBase):
    pass

class Component(ComponentInstall):
    id: str
    instalation_maintenance_id: str
    installed_at: datetime