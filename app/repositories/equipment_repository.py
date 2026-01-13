from enums import DepartmentEnum, EquipmentStatusEnum
from schemas.equipment import EquipmentCreate
from psycopg2.extras import RealDictCursor
from repositories.base_repository import BaseRepository

class EquipmentRepository(BaseRepository):
    def __init__(self, connection):
        self.conn = connection

    def get(
        self,
        ean: str | None = None,
        department: DepartmentEnum | None = None,
        status: EquipmentStatusEnum | None = None
    ):
        cursor = self.conn.cursor()

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

    def get_by_id(self, id: str):
        cursor = self.conn.cursor()

        equipment_sql = """
            SELECT
                e.id, 
                e.name, 
                e.ean, 
                es.name as status, 
                d.name as location
            FROM equipments e
            JOIN equipment_status es ON es.id = e.equipment_status_id 
            JOIN departments d ON d.id = e.department_id
            WHERE e.id = %s
        """

        cursor.execute(equipment_sql, (id,))
        equipment = cursor.fetchone()

        if not equipment:
            return None

        sql_moves = """
            SELECT  
                previously_located_at as from, 
                newly_alocated_at as to,
                created_at as date
            FROM equipment_moves
            WHERE equipment_id = %s
            ORDER BY date DESC
            LIMIT 5
        """
        cursor.execute(sql_moves, (equipment['id'],))
        moves = cursor.fetchall()

        sql_maintenances = """
            SELECT
                m.description,
                me.created_at as date,
                u.firstname as technician
            FROM maintenance_equipments me
            JOIN maintenances m ON m.id = me.maintenance_id
            JOIN users u ON m.responsible_id = u.id
            WHERE me.equipment_id = %s
            ORDER BY date
            LIMIT 3
        """
        cursor.execute(sql_maintenances, (equipment['id'],))
        maintenances = cursor.fetchall()

        response_data = dict(equipment)
        response_data["history_moves"] = moves
        response_data["history_maintenances"] = maintenances

        return response_data

    def add(self, equipment: EquipmentCreate):
        data = equipment.model_dump(exclude_unset=True)
        cols, placeholders, vals = self._prepare_insert(data)

        print(cols)
        print(vals)

        query = f"""
            INSERT INTO equipments 
            ({cols}) 
            VALUES
            ({placeholders})
            RETURNING *
        """

        cursor = self.conn.cursor()
        cursor.execute(query, vals)
        self.conn.commit()

        return cursor.fetchone()