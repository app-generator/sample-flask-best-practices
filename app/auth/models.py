import jwt
from app import db
from time import time
from flask import current_app
from flask_login import UserMixin
from sqlalchemy.orm.exc import NoResultFound
from werkzeug.security import check_password_hash, generate_password_hash

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(128), nullable=False, unique=True)
    password = db.Column(db.String(54), nullable=False)
    active = db.Column(db.SmallInteger, nullable=False, default=True)

    created_at = db.Column(db.DateTime, default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.set_password(password)

    def __repr__(self):
        return '<User %s>' % self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_reset_password_token(self, expires_in=600):
        """
        This function generates a time based expiration jwt that is used in the reset password scenario,
        incase if user does not use link in defined time the link would expire
        :param expires_in: time in which the jwt expires
        :return: web token
        """
        return jwt.encode({'reset_password': self.id,
                           'exp': time() + expires_in},
                          current_app.config['SECRET_KEY'],
                          algorithm='HS256').decode('utf-8')

    @classmethod
    def get(cls, user_id):
        """
        :rtype: object
        :type user_id: int
        """
        try:
            return User.query.filter_by(id=user_id).one()
        except NoResultFound:
            return None