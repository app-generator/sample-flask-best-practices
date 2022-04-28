from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user

from app import bcrypt, db, login_manager, security
from app.auth.forms import LoginForm, RegisterForm
from app.auth.models import User
from flask_talisman import Talisman, ALLOW_FROM


auth = Blueprint('auth', __name__)


@login_manager.user_loader
@auth.route('/login', methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM, frame_options_allow_from='*')
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = LoginForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        remember = form.remember.data
        user = User.query.filter_by(username=username).first()
        if bcrypt.check_password_hash(user.password, password):
            login_user(user, remember=remember)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Password incorrect', category='danger')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have logged out now.', category='info')
    return redirect(url_for('auth.login'))


@auth.route('/register', methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM, frame_options_allow_from='*')
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        email = form.email.data
        user = User(username=username, password=password, email=email)
        db.session.add(user)
        db.session.commit()
        flash('Congrats, register success. You can log in now.', category='info')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

