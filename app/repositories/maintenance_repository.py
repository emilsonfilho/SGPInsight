from enums import MaintenanceStatusEnum

class MaintenanceRepository:
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
        