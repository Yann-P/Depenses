from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *
from models.User import User
import sys


user = Blueprint('user', __name__, template_folder='templates')


@user.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@user.route('/login', methods=['GET'])
def login():
    return render_template('user/login.html')

@user.route('/logout', methods=['GET'])
def logout():
    session['uid'] = None
    return redirect(url_for('user.login'))
 
@user.route('/login', methods=['POST'])
def login_form():
    name = request.form.get('name')
    password = request.form.get('password')
    is_new_user = not User.exists(name)

    if name: 
        if not password:
            return render_template('user/login.html', 
                step2=True, 
                newuser=is_new_user, 
                name=name) 
        else:
            # now can handle login
            if is_new_user:
                return handle_signup(name, password)
            else:
                return handle_login(name, password)

    return render_template('user/login.html')

def handle_login(name, password):
    uid = User.login(name, password)
    if uid != -1: # login successful
        session['uid'] = uid
        return redirect(url_for('dashboard.index'))
    else:
        return render_template('user/login.html', step2=True, newuser=False, name=name, error=True)

def handle_signup(name, password):
    print('spam')
    user = User.insert(name, password)
    session['uid'] = user.id
    return redirect(url_for('dashboard.index'))