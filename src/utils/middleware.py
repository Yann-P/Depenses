from functools import wraps
from flask import g, redirect, url_for, request


def require_user(f):
    @wraps(f)
    def callback(*args, **kwargs):
        if g.user is None:
            if not request.is_xhr:
                return redirect(url_for('user.login'))
            return '403 Not An User', 403
        return f(*args, **kwargs)
    return callback