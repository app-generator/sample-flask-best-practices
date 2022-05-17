import unittest

from app import create_app, db, bcrypt
from app.auth.models import User


class TestUserLogin(unittest.TestCase):

    def setUp(self):
        self.app = create_app("testing")
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_user(self):
        user = User(username='username', email='user@email.com', password='password')
        db.session.add(user)
        db.session.commit()
        assert len(User.query.all()) == 1

    def test_check_password(self):
        user = User(username='username', email='user@email.com', password='password')
        db.session.add(user)
        db.session.commit()
        user = User.query.filter_by(username='username').first()
        assert bcrypt.check_password_hash(user.password, 'password')


if __name__ == '__main__':
    unittest.main()