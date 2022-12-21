# create a InMemoryUserRepository class implementing UserRepository

from app.repositories.user_repository import UserRepository
from common.hashed import calcHashedPassword


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.users = []

    def create(self, username, password):
        hashedPassword = calcHashedPassword(password)
        return {'username': username, 'password': hashedPassword}

    def get_by_id(self, username):
        for user in self.users:
            if user.username == username:
                return user

    def update(self, user):
        for index, u in enumerate(self.users):
            if u.username == user.username:
                self.users[index] = user

    def delete(self, username):
        for index, user in enumerate(self.users):
            if user.username == username:
                del self.users[index]