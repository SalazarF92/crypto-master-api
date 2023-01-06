from flask_jwt_extended import JWTManager, get_jwt_identity, jwt_required



class CryptoController:
    def __init__(self, app, conn):
        self.app = app
        self.jwt = JWTManager(self.app)
        
        @self.app.route("/crypto", methods=["GET"])
        def get_crypto():
            
            return 'cryptei'
            # return self.user_service.get_users()
            
        @self.app.route("/crypto2", methods=["GET"])
        @jwt_required()
        def get_crypto1():
            return 'cryptei2'
            # return self.user_service.get_users()