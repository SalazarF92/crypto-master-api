from common.hashed import validatePassword
from tests.services.in_memory_user_repository import InMemoryUserRepository

userRepository = InMemoryUserRepository()
username = "username"
password = "password"

def test_create_user():
    
    user = userRepository.create(username, password)
    assert user['username'] == "username"
    

def test_login():
    
    user = userRepository.create(username, password)
    assert user['username'] == "username"
    assert validatePassword(password, user['password']) == True
    
    
    
    
   

    
    

    