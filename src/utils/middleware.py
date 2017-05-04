from functools import wraps
from flask import g, redirect, url_for, request
from models.Team import Team


def require_user(f):
    @wraps(f)
    def callback(*args, **kwargs):
        if g.user is None:
            if not request.is_xhr:
                return redirect(url_for('user.login'))
            return '403 Not An User', 403
        return f(*args, **kwargs)
    return callback

def current_user_belongs_to_team(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        json_data = request.get_json()
        if "tid" in kwargs and not Team.from_id(kwargs['tid']).contains_user(g.user.id):
            return '403 Forbidden', 403
        return func(*args, **kwargs)
    return wrapper