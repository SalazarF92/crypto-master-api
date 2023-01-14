## implesment abstract class in UserRepositoryDB class
from src.app.repositories.user_repository import UserRepository


class UserRepositoryDB(UserRepository):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def get_by_id(self, user_id):
        return "oi"
        # return self.conn.query(User).filter(User.id == user_id).first()

    def get_users(self):
        query = "SELECT * FROM users"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result

    def get_me(self, username, withPassword):
        if withPassword:
            query = "SELECT * FROM users WHERE username = %s"
            self.cursor.execute(query, (str(username),))
            result = self.cursor.fetchone()
            return result

        query = "SELECT id, username FROM users WHERE username = %s "
        self.cursor.execute(query, (username,))
        result = self.cursor.fetchone()
        return result

    def create(self, username, password):
        ## generate id automatic
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        user = self.cursor.execute(query, (username, password))
        self.conn.commit()
        return user["id"]

    def update(self, user):
        self.conn.merge(user)
        self.conn.commit()
        return user

    def delete(self, user):
        self.conn.delete(user)
        self.conn.commit()
        return user
