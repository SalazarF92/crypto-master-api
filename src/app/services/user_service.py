

from src.common.hashed import calcHashedPassword
from src.database.repositories.user_repository_db import UserRepositoryDB


class UserService:
    def __init__(self, conn):
        self.conn = conn
        self.userRepository = UserRepositoryDB(conn)
    
    
    def create(self, username, password):
        hashedPassword = calcHashedPassword(password)
        return self.userRepository.create(username, hashedPassword)