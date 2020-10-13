# python

# packages
from flask import Blueprint
from flask import current_app
from flask import jsonify
from flask import render_template
from flask import request
from flask import session

# local
from app.extensions import db

bp = Blueprint('subfolder', __name__, url_prefix='/subfolder')


@bp.before_request
def task_before_request():
    # runs before this blueprint routes only
    # check for permission and stuff
    pass


@bp.route('/')
def subfolder_index():
    return render_template('subfolder/index.html')
