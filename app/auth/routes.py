from is_safe_url import is_safe_url
from flask_login import login_user, logout_user, current_user
from flask import Blueprint, render_template, request, flash, redirect, url_for, abort

from app import bcrypt, db, login_manager, security

from app.auth.models import User
from flask_talisman import Talisman, ALLOW_FROM
from validate_email_address import validate_email
from app.auth.email import send_password_reset_email
from app.auth.forms import LoginForm, RegisterForm, ResetPasswordRequestForm, ResetPasswordForm

from app.utils import _log_message_
auth = Blueprint('auth', __name__)


@login_manager.user_loader
@auth.route('/login',
            methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM,
                      frame_options_allow_from='*')
def login():
    """
        This is the login route corresponding to the `/login` route,
        the `login_manager.user_loader` loads the current user into the function,
        also as security measure are the talisman/rate-limiter on the end-points in place for more info:
                <i>     https://flask-limiter.readthedocs.io/en/stable/
                <ii>    https://github.com/GoogleCloudPlatform/flask-talisman
        :return: Logged in page rendered on the specified template `templates/auth/login.html`
    """
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
            next_ = request.args.get('next')
            if not is_safe_url(next):
                return abort(400)
            else:
                return redirect(next_ or url_for('main.index'))
        else:
            flash('Password incorrect', category='danger')
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
def logout():
    logout_user()
    flash('You have logged out now.', category='info')
    return redirect(url_for('auth.login'))


@auth.route('/register',
            methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM,
                      frame_options_allow_from='*')
def register():
    """
        This is the register route corresponding to the `/register` route,
        this function creates the new user and creates them in the specified db configuration
        also as security measure are the talisman/rate-limiter on the end-points in place for more info:
                <i>     https://flask-limiter.readthedocs.io/en/stable/
                <ii>    https://github.com/GoogleCloudPlatform/flask-talisman
        :return: Logged in page rendered on the specified template `templates/auth/register.html`
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = RegisterForm(request.form)
    if form.validate_on_submit():
        username = form.username.data
        password = bcrypt.generate_password_hash(form.password.data)
        email = form.email.data
        user = User(username=username,
                    password=password,
                    email=email)
        if validate_email(email, verify=True):
            db.session.add(user)
            db.session.commit()
        else:
            flash('Email is not valid or does not exists.', category='danger')
            return redirect(url_for('auth.register'))
        flash('Congrats, register success. You can log in now.', category='info')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)

@auth.route('/reset_password/<token>', methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM,
                      frame_options_allow_from='*')
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm(request.form)
    if form.validate_on_submit():
        user = User.verify_reset_password_token(token)
        user.password = bcrypt.generate_password_hash(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password.html', form=form)

@auth.route('/send_reset_password_request', methods=['GET', 'POST'])
@security["talisman"](frame_options=ALLOW_FROM,
                      frame_options_allow_from='*')
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('auth.login'))
    form = ResetPasswordRequestForm(request.form)
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/reset_password_request.html', form=form)



