from flask import request
from src.app.services.user_crypto_service import UserCryptoService
from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required

route = "/crypto"

class UserCryptoController:
    def __init__(self, app, conn):
        self.app = app
        self.jwt = JWTManager(self.app)
        self.user_crypto_service = UserCryptoService(conn)
        
        @self.app.route(f'{route}/list', methods=["GET"])
        def get_crypto_list():
            user_id = get_jwt_identity()
            return self.user_crypto_service.get_crypto_list()
        
        @self.app.route(f'{route}/user_list', methods=["GET"])
        @jwt_required()
        def get_user_list():
            user_id = get_jwt_identity()
            return self.user_crypto_service.get_user_list(user_id)
            
        @self.app.route(f'{route}/add', methods=["POST"])
        @jwt_required()
        def add():
            user_id = get_jwt_identity()
            result =  self.user_crypto_service.add(user_id, request.json['symbol'])
            return result
            
