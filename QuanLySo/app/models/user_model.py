class User:
    def __init__(self, username):
        self.username = username

    def get_data(self):
        return {"username": self.username}