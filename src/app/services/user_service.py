

from src.common.hashed import calcHashedPassword, validatePassword
from src.database.repositories.user_repository_db import UserRepositoryDB
from flask_jwt_extended import create_access_token


class UserService:
    def __init__(self, conn):
        self.conn = conn
        self.user_respository = UserRepositoryDB(conn)
    
    
    def create(self, username, password):
        hashedPassword = calcHashedPassword(password)
        return self.user_respository.create(username, hashedPassword)

    def get_me(self, username, withPassword):
        return self.user_respository.get_me(username, withPassword)
    
    def get_users(self):
        return self.user_respository.get_users()
    
    def login(self, username, password):
        user = self.user_respository.get_me(username, True)
        
        
        ## if user is None throw erro r
        if user is None:
            return 'User not found', 404

        
        hashedPassword = validatePassword(password, user[2])
        
        if hashedPassword:
            return self.generate_token(user), 200
        
        else :
            return 'Wrong password', 401
        
        
    
    def generate_token(self, user):
        return create_access_token(identity=user[0])