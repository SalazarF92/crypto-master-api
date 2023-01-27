#create abstract class for user repository

from abc import ABC, abstractmethod

class UserCryptoRepository(ABC):
    @abstractmethod
    def get_crypto_list(self, username, password):
        pass

    @abstractmethod
    def get_crypto_user(self, username):
        pass
    
    @abstractmethod
    def add(self, user_id, crypto_symbol):
        pass
    
    