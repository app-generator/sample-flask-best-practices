from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/index')
@login_required
def index():
    return render_template('main/index.html')