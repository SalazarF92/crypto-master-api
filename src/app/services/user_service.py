

from src.common.hashed import calcHashedPassword
from src.database.repositories.user_repository_db import UserRepositoryDB


class UserService:
    def __init__(self, conn):
        self.conn = conn
        self.user_respository = UserRepositoryDB(conn)
    
    
    def create(self, username, password):
        hashedPassword = calcHashedPassword(password)
        return self.user_respository.create(username, hashedPassword)
    
    def get_users(self):
        print('to aqui')
        return self.user_respository.get_users()