from flask import Flask
from flask_mail import Mail
from app.config import config
from flask_minify import Minify
from flask_bcrypt import Bcrypt
from flask_session import Session
from flask_login import LoginManager
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect
from flask_sqlalchemy import SQLAlchemy
from app.setup_security import setup_security_measure_on_application

# Setup Bootstrap5 on app
bootstrap = Bootstrap5()

# Set up Brycpt on the app
bcrypt = Bcrypt()

# Set up SQL alchemy
db = SQLAlchemy()

# Set up Flask-login
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'auth.signin'

# Setup CSRF
csrf = CSRFProtect()

# Security Measures dict initially None
security = None

# Setup mailer
mail = Mail()

def create_app(config_name):
    """For to use dynamic environment"""
    global security
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    bcrypt.init_app(app)
    security = setup_security_measure_on_application(app)
    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)
    csrf.init_app(app)
    mail.init_app(app)
    Minify(app=app, html=True, js=True, cssless=True)
    Session(app)

    from app.auth.routes import auth
    app.register_blueprint(auth)

    return app
