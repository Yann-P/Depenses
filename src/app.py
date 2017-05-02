#! /usr/bin/python3.4

"""
    Depenses
    Software to share a budget in a group.

    :copyright: (c) 2017 by Yann Pellegrini.
    :license: GPLv3, see LICENSE for more details.
"""

from datetime import datetime
from flask import Flask, request, session, url_for, redirect, \
     render_template, abort, g
from controllers.user import user
from models.User import User


app = Flask('depenses')
app.register_blueprint(user, url_prefix='/user')
app.secret_key = 'd1\x01O<!\xd5\xa2\xa0\x9fR"'

@app.before_request
def before_request():
    g.user = None
    if 'uid' in session:
        g.user = User.from_id(session['uid'])


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
