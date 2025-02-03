class User:
    def __init__(self, username):
        self.__username = username
        self.__email = f"{self.__username}@example.com"
    @property
    def username(self):
        return self.__username
    @property
    def email(self):
        return self.__email
    def __str__(self):
        return f"User: {self.username} - Email: {self.email}"
    def __dict__(self):
        return {
            "username": self.username,
            "email": self.email
        }
