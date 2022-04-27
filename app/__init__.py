from flask import Flask
from app.config import config
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from app.setup_security import setup_security_measure_on_application


# Set up SQL alchemy
db = SQLAlchemy()

# Set up Flask-login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'

def create_app(config_name):
    """For to use dynamic environment"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    security = setup_security_measure_on_application(app)


    db.init_app(app)
    login_manager.init_app(app)
    return app, security

app, security = create_app("development")
print(app.config)
