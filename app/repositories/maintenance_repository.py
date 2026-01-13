from enums import MaintenanceStatusEnum
from schemas.maintenance import MaintenanceCreate
from .base_repository import BaseRepository

class MaintenanceRepository(BaseRepository):
    def __init__(self, connection):
        self.conn = connection

    def get(
        self,
        status: MaintenanceStatusEnum | None = None,
        responsible_id: str | None = None
    ):
        cursor = self.conn.cursor()

        sql = "SELECT * FROM maintenances"
        conditions = []
        params = []

        if status:
            if status is MaintenanceStatusEnum.ACTIVE:
                conditions.append("finished_at IS NULL")
            else:
                conditions.append("finished_at IS NOT NULL")
            
        if responsible_id:
            conditions.append("responsible_id = %s")
            params.append(responsible_id)

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)
        
        cursor.execute(sql, params)

        return cursor.fetchall()
    
    def add(self, maintenances: MaintenanceCreate):
        cursor = self.conn.cursor()

        try:

            maintenance_data = maintenances.model_dump(exclude={'equipment_ids'}, exclude_unset=True)
            equipment_ids = maintenances.equipment_ids 

            cols, placeholders, vals = self._prepare_insert(maintenance_data)

            query_maintenance = f"""
                INSERT INTO maintenances
                ({cols})
                VALUES
                ({placeholders})
                RETURNING *
            """

            cursor.execute(query_maintenance, vals)
            new_maintenance = cursor.fetchone()
            new_maintenance_id = new_maintenance['id']

            if equipment_ids:
                query_link = """
                    INSERT INTO maintenance_equipments (maintenance_id, equipment_id)
                    VALUES (%s, %s)
                """

                link_values = [(new_maintenance_id, equip_id) for equip_id in equipment_ids]
                cursor.executemany(query_link, link_values)

            self.conn.commit()

            return new_maintenance
        except Exception as e:
            self.conn.rollback()
            raise e
            
        