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
from flask_babel import Babel
from controllers.user import user
from controllers.team import team
from controllers.dashboard import dashboard

from models.User import User
import os


app = Flask('depenses', template_folder=os.path.join(os.path.dirname(__file__), "templates"))

app.register_blueprint(user, url_prefix='/user')
app.register_blueprint(team, url_prefix='/team')
app.register_blueprint(dashboard, url_prefix='/dashboard')

###########################################
app.secret_key = 'PLEASE_CHANGE_ME_!!!!!' # <= CHANGE THIS !!!
###########################################

babel = Babel(app)

app.config['BABEL_TRANSLATION_DIRECTORIES'] = os.path.join(os.path.dirname(__file__), "../langs/translations")

@babel.localeselector
def get_locale():
	return request.accept_languages.best_match(['en', 'fr'])

@app.before_request
def before_request():
	session.permanent = True
	g.user = None
	if 'uid' in session and session['uid']:
		g.user = User.from_id(session['uid'])


@app.route('/')
def index():
	if not g.user:
		return render_template('index.html')
	return redirect(url_for('dashboard.index'))


if __name__ == '__main__':
	app.run(debug=True, host="0.0.0.0", port=80)
