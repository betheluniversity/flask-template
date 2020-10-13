# packages
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import render_template
from flask import request
from flask import session

# project
from app.controllers import get_user

# import other blueprints with aliases
from .subfolder import bp as subfolder_bp


bp = Blueprint('app', __name__)


@current_app.before_request
def before_request():
    # runs for the entire app. Check for persmissions, etc

    if 'username' not in session.keys():
        get_user()


@bp.route('/')
def index():
    return render_template('index.html')