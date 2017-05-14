from functools import wraps
from flask import g, redirect, url_for, request, abort
from models.Team import Team


def require_user(f):
	@wraps(f)
	def callback(*args, **kwargs):
		if g.user is None:
			return redirect(url_for('user.login'))
		return f(*args, **kwargs)
	return callback

def current_user_belongs_to_team(func):
	@wraps(func)
	def wrapper(*args, **kwargs):
		json_data = request.get_json()
		if "tid" in kwargs:
			team = Team.from_id(kwargs['tid'])
			if team and not team.contains_user(g.user.id):
				return redirect(url_for('user.login'))
		return func(*args, **kwargs)
	return wrapper