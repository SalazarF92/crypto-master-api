from src.http.controllers.user_crypto_controller import UserCryptoController
from src.http.controllers.user_controller import UserController

class Router:
    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        
        
    def user_controller(self, app, conn):
        UserController(app, conn)
        
    def user_crypto_controller(self, app, conn):
        UserCryptoController(app, conn)
        
        
    def run(self):
        self.user_controller(self.app, self.conn)
        self.user_crypto_controller(self.app, self.conn)
        self.app.run()
        
