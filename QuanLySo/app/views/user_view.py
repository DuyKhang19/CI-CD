from flask import Blueprint, render_template
from app.controllers.user_controller import get_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/")
def home():
    user = get_user("John Doe")
    return render_template("index.html", user=user)