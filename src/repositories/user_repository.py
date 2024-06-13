from src.models.user import User

class UserRepository:
    def __init__(self):
        self.users = [
            User(1, "John Doe", "john@example.com"),
            User(2, "Jane Doe", "jane@example.com")
        ]

    def get_users(self):
        return self.users