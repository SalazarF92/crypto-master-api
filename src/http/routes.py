from src.http.controllers.crypyo_controller import CryptoController
from src.http.controllers.user_controller import UserController

class Router:
    def __init__(self, app, conn):
        self.app = app
        self.conn = conn
        
        
    def user_controller(self, app, conn):
        UserController(app, conn)
        
    def crypto_controller(self, app, conn):
        CryptoController(app, conn)
        
        
        
    def run(self):
        self.user_controller(self.app, self.conn)
        self.crypto_controller(self.app, self.conn)
        self.app.run()
        
