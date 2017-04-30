from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *


user = Blueprint('user', __name__, template_folder='templates')


# TODO SWITCH TO https://pythonhosted.org/oursql/install.html#using-pip
# OURSQL

@user.route('/login', methods=['GET'])
def login():
    cur = db.cursor()
    cur.execute("SELECT * FROM user WHERE role = %d", (1,))
    return str(cur.fetch_all())