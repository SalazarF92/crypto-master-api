## implesment abstract class in UserRepositoryDB class
from src.app.repositories.user_crypto_repository import UserCryptoRepository


class UserCryptoRepositoryDB(UserCryptoRepository):
    def __init__(self, conn):
        self.conn = conn
        self.cursor = conn.cursor()

    def get_crypto_list(self):
        query = "SELECT * FROM coin"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        return result
    
    def get_by_symbol(self, user_id, coin_symbol):
        query = "SELECT * FROM user_coin WHERE coin_symbol = %s AND user_id = %s"
        self.cursor.execute(query, (coin_symbol, user_id,))
        result = self.cursor.fetchone()
        if result:
            return True
        return False

    def get_crypto_user(self, user_id):
        ## create a query to select from user_id with inner join info from coin table
        query2 = "SELECT * FROM user_coin INNER JOIN coin ON user_coin.coin_symbol = coin.symbol WHERE user_coin.user_id = %s"
        # query = "SELECT * FROM user_coin where user_id = %s"
        self.cursor.execute(query2, (user_id,))
        result = self.cursor.fetchall()
        return result


    def add(self, user_id, coin_symbol):
        query = "INSERT INTO user_coin (user_id, coin_symbol) VALUES (%s, %s)"
        self.cursor.execute(query, (user_id, coin_symbol,))
        self.conn.commit()
        return True
        
