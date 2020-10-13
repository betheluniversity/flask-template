from flask import current_app
from flask import request


def get_user():
    if current_app.config['ENVIRON'] == 'prod':
        username = request.environ.get('REMOTE_USER')
    else:
        username = current_app.config['TEST_USER']

    session['username'] = username
