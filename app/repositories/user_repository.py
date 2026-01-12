from schemas.user import UserLogin


class UserRepository:
    def __init__(self, connection):
        self.conn = connection
        
    def login(self, login_data):
        cursor = self.conn.cursor()
        
        sql = """
            SELECT id, firstName, lastName, email, role_id, password, disabled FROM users WHERE email = ?
        """
        values = login_data.username,
            
        cursor.execute(sql, values)
        row = cursor.fetchone()
        
        if not row:
            return None
        
        return UserLogin(**dict(row))
