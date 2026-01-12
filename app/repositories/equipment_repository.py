from enums import DepartmentEnum, EquipmentStatusEnum
from psycopg2.extras import RealDictCursor

class EquipmentRepository:
    def __init__(self, connection):
        self.conn = connection

    def get(
        self,
        ean: str | None = None,
        department: DepartmentEnum | None = None,
        status: EquipmentStatusEnum | None = None
    ):
        cursor = self.conn.cursor(cursor_factory=RealDictCursor)

        sql = "SELECT * FROM equipments"
        conditions = []
        params = []

        if ean:
            conditions.append("ean = %s")
            params.append(ean)

        if department:
            conditions.append("department_id = %s")
            params.append(department)

        if status:
            conditions.append("equipment_status_id = %s")
            params.append(status)

        if conditions:
            sql += " WHERE " + " AND ".join(conditions)

        cursor.execute(sql, params)

        return cursor.fetchall()