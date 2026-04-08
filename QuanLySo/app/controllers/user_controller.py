from app.models.user_model import User

def get_user(username):
    user = User(username)
    return user.get_data()