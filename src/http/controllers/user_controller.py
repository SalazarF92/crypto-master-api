from src.app.services.user_service import UserService
from flask_jwt_extended import JWTManager
from flask import request

class UserController:
    def __init__(self, app, conn):
        self.app = app
        self.jwt = JWTManager(self.app)
        self.user_service = UserService(conn)
        
        #template endpoints with user in prefix
        route = "/user"
        
        
        @self.app.route(f'{route}/create', methods=["POST"])
        def create():
            try :
                username = request.json['username']
                password = request.json['password']
                print('ate aqui eu vim')
                response = self.user_service.create(username, password)
                #return a response as json response 
                return response
            except Exception as e:
                return str(e)
            
        @self.app.route(f'{route}/users2', methods=["GET"])
        def get_users():
            return self.user_service.get_users()
