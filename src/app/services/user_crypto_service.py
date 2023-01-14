from src.database.repositories.user_crypto_repository_db import UserCryptoRepositoryDB


class UserCryptoService:
    def __init__(self, conn):
        self.conn = conn
        self.user_crypto_respository = UserCryptoRepositoryDB(conn)

    def get_crypto_list(self):
        return self.user_crypto_respository.get_crypto_list()
    
    def get_user_list(self, user_id):
        return self.user_crypto_respository.get_crypto_user(user_id)
        
    def add(self, user_id, crypto_symbol):
        coin_exists = self.user_crypto_respository.get_by_symbol(user_id, crypto_symbol)
        if coin_exists:
            return 'Coin already in list'        
        result = self.user_crypto_respository.add(user_id, crypto_symbol)
        if result:
            return 'Coin added'
