#create abstract class for user repository

from abc import ABC, abstractmethod

class UserRepository(ABC):
    @abstractmethod
    def create(self, username, password):
        pass

    @abstractmethod
    def get_by_id(self, username):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def delete(self, username):
        pass