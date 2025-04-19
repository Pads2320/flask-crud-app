# app/__init__.py
from flask import Flask
from app.extensions import db
from app.routes.user import users_bp  # import blueprints
from app.models import User  # force model import for table creation

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    app.register_blueprint(users_bp)

    with app.app_context():
        db.create_all()

    return app
