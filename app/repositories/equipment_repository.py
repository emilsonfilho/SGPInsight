from enums import DepartmentEnum, EquipmentStatusEnum
from schemas.equipment import EquipmentCreate, EquipmentMoveCreate
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
    
    def update(self, equipment_id: str, equipment: EquipmentCreate):
        data = equipment.model_dump(exclude_unset=True)
        
        set_str, vals = self._prepare_update(data)

        query = f"""
            UPDATE equipments
            SET {set_str}
            WHERE id = %s
        """

        vals.append(equipment_id)

        cursor = self.conn.cursor()
        cursor.execute(query, vals)
        self.conn.commit()

        if cursor.rowcount == 0:
            return None

        data['id'] = equipment_id
        return data

    def move(self, equipment_id: str, move: EquipmentMoveCreate):
        cursor = self.conn.cursor()
        
        try:
            sql_get_current = "SELECT department_id FROM equipments WHERE id = %s"
            cursor.execute(sql_get_current, (equipment_id,))
            equipment = cursor.fetchone()

            if not equipment:
                raise ValueError("Equipamento não encontrado")

            previous_department_id = equipment['department_id']

            data = move.model_dump()

            sql_update = """
                UPDATE equipments
                SET department_id = %s
                WHERE id = %s
            """

            cursor.execute(sql_update, (data['newly_alocated_at'], equipment_id))

            data['equipment_id'] = equipment_id
            data['previously_located_at'] = previous_department_id
            cols, placeholders, vals = self._prepare_insert(data)

            sql_insert = f"""
                INSERT INTO equipment_moves
                ({cols})
                VALUES
                ({placeholders})
                RETURNING *
            """

            cursor.execute(sql_insert, vals)
            self.conn.commit()

            return cursor.fetchone()
        except Exception as e:
            self.conn.rollback()
            raise e