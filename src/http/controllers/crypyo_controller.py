from flask_jwt_extended import JWTManager



class CryptoController:
    def __init__(self, app, conn):
        self.app = app
        jwt = JWTManager(self.app)
        
        @self.app.route("/crypto", methods=["GET"])
        def get_crypto():
            
            return 'cryptei'
            # return self.user_service.get_users()
            
        @self.app.route("/crypto2", methods=["GET"])
        def get_crypto1():
            return 'cryptei2'
            # return self.user_service.get_users()