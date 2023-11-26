# /app/controllers.py
from app.models import User

def get_users():
    users = [
        User('user1', 'user1@example.com'),
        User('user2', 'user2@example.com'),
    ]
    return users
