from enum import Enum

class EquipmentStatusEnum(str, Enum):
    OPERATIONAL_FIELD = "ad10386e-4409-4f85-ab66-86fc68e43967"
    OPERATIONAL_OFFICE = "7928f418-b6ec-4678-a8a1-62523e746509"
    MAINTENANCE_LAB = "4f7e4913-d84c-4c4e-8590-ab042f2ffa62"
    MAINTENANCE_OUTSOURCED = "69dc98bb-cad1-41b8-a34a-d741b01a6475"
    AWAITING_CONFIGURATION = "106bff4e-37e0-4100-a3ea-3ae3a655f76f"
    AWAITING_DISPOSAL = "c1df3c71-6cf7-45c0-98fa-b6ae87d2f53f"
    DISPOSED = "3fde1877-6862-4e93-a513-6720b4531d21"
    STOCK_READY = "4a6dbd66-944e-46c4-9288-7b6338196814"
    STOCK_RESERVE = "b0de06e6-065d-4d00-83d5-0a88654d0a7a"

    @classmethod
    def from_keyword(cls, keyword: str | None):
        if not keyword:
            return None

        mapping = {
            "campo_operacional": cls.OPERATIONAL_FIELD,
            "escritorio_operacional": cls.OPERATIONAL_OFFICE,
            "laboratorio": cls.MAINTENANCE_LAB,
            "terceirizado": cls.MAINTENANCE_OUTSOURCED,
            "esperando_configuracao": cls.AWAITING_CONFIGURATION,
            "esperando_descarte": cls.AWAITING_DISPOSAL,
            "descartado": cls.DISPOSED,
            "pronto": cls.STOCK_READY,
            "reserva": cls.STOCK_RESERVE
        }

        return mapping.get(keyword.lower())

    @property
    def label(self):
        labels = {
            self.OPERATIONAL_FIELD: "Operacional (Campo)",
            self.OPERATIONAL_OFFICE: "Operacional (Escritório)",
            self.MAINTENANCE_LAB: "Em Manutenção (Laboratório)",
            self.MAINTENANCE_OUTSOURCED: "Em Manutenção (Terceirizada)",
            self.AWAITING_CONFIGURATION: "Aguardando Configuração",
            self.AWAITING_DISPOSAL: "Aguardando Descarte",
            self.DISPOSED: "Descartado",
            self.STOCK_READY: "Em Estoque (Pronto)",
            self.STOCK_RESERVE: "Em Estoque (Reserva)"
        }
        return labels.get(self, "Desconhecido")

class RoleEnum(str, Enum):
    MANAGER = "2f87ad2e-1fd2-49bb-a2a9-789841d64de5"
    ANALYST = "22a544a1-1493-4509-885d-b16745509b2e"
    INTERN = "c4a0674c-7643-4737-a274-9955c52aedd5"

    @property
    def label(self):
        labels = {
            RoleEnum.MANAGER: "Gerente",
            RoleEnum.ANALYST: "Analista",
            RoleEnum.INTERN: "Estagiário"
        }

        return labels.get(self)

class DepartmentEnum(str, Enum):
    CONSTRUCTION_SITE_PROJECT_ALPHA = "d9cd69c2-7690-4d3f-baae-ea8e96e323aa"
    CONSTRUCTION_SITE_PROJECT_BETA = "e8841c8d-5641-4349-a3b6-6a5d53fb475a" 
    SITE_ENGINEERING_OFFICE = "5537e1f0-9480-405b-87fb-dba79ec6ffa1"
    FIELD_IT_SUPPORT = "9bdbcb3c-1aad-4179-994c-29ab4a50f58f" 
    IT_LOGISTICS_WAREHOUSE = "5adfd3e0-50bc-4b37-a216-799a818feedb" 
    ASSET_MANAGEMENT = "5dea7663-05bb-43b2-9f75-ac92fe4140dd" 
    COMMERCIAL_DEPARTMENT = "8249748d-8320-4e99-84a0-cba81a38615a" 
    HUMAN_RESOURCES = "da3791af-165e-4766-bf95-2e047dd85074" 
    FINANCE_CONTROLLERSHIP = "b6e07ea4-527c-4731-bdbf-bd501b2a1807" 
    CONFIGURATION_REPAIR_LAB = "24616230-a688-491b-8e99-2fe51d2d324e"

    @property
    def label(self):
        # Descrições legíveis para UI/Relatórios
        labels = {
            self.CONSTRUCTION_SITE_PROJECT_ALPHA: "Canteiro de Obras - Projeto Alpha",
            self.CONSTRUCTION_SITE_PROJECT_BETA: "Canteiro de Obras - Projeto Beta",
            self.SITE_ENGINEERING_OFFICE: "Escritório de Engenharia",
            self.FIELD_IT_SUPPORT: "Suporte Técnico de Campo",
            self.IT_LOGISTICS_WAREHOUSE: "Almoxarifado e Logística de TI",
            self.ASSET_MANAGEMENT: "Gestão de Ativos",
            self.COMMERCIAL_DEPARTMENT: "Departamento Comercial",
            self.HUMAN_RESOURCES: "Recursos Humanos (RH)",
            self.FINANCE_CONTROLLERSHIP: "Financeiro e Controladoria",
            self.CONFIGURATION_REPAIR_LAB: "Laboratório de Manutenção e Configuração"
        }
        return labels.get(self)

class MaintenanceStatusEnum(Enum):
    ACTIVE = "active"
    CLOSED = "closed"

    @classmethod
    def from_keyword(cls, keyword: str | None):
        if not keyword:
            return None
        
        mapping = {
            "ativo": cls.ACTIVE,
            "fechado": cls.CLOSED
        }

        return mapping.get(keyword.lower())
    
class ComponentStatusEnum(str, Enum):
    IN_STOCK_NEW = '25e8d8d4-27b0-4d8f-8f31-5dd30b6bd0b3'
    IN_STOCK_REFURBISHED = '592b845e-70bf-49c0-972d-6c9abb9ed0fc'
    INSTALLED_OPERATIONAL = 'f38ba039-adff-448c-be88-f3350841344b'
    INSTALLED_DEGRADED = '5d051672-891f-44b3-ac53-d0161b9d396b'
    MAINTENANCE_INTERNAL = 'f490b04f-4970-4198-a302-d961900a17a1'
    MAINTENANCE_OUTSOURCED = 'bfd63434-fc36-4def-b916-d2835e2c7dd4'
    AWAITING_DISPOSAL = '92f8e4bd-4620-4605-9e08-fc922512ab23'
    DISCARDED_SCRAP = '82535b4f-cf54-4294-a0d4-9d8ed409f3f6'
    RETURNED_TO_SUPPLIER = '9a01331e-ea71-4362-8059-bd35ce42d07a'
    QUALITY_TESTING = 'd0f89642-9ed7-482a-a1b0-9abfd960ddfa'