from .base import Base
from enums import ReplacementEnum
from datetime import datetime

class ComponentBase(Base):
    component_id: str
    equipment_id: str
    
class ComponentInstall(ComponentBase):
    observations: str

class ComponentRemove(ComponentBase):
    observations: str | None = None

class Component(ComponentInstall):
    id: str
    instalation_maintenance_id: str
    installed_at: datetime