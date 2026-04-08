from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Register blueprints
    from app.views.user_view import user_bp
    app.register_blueprint(user_bp)

    return app