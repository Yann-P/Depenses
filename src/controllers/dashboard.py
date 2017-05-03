from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *
from models.User import User
from models.Team import Team
from utils.middleware import *
import sys


dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/', methods=["get"])
@require_user
def index():
	return render_template('dashboard/index.html', own_expenditures=g.user.get_expenditures())

@dashboard.route('/teams', methods=['get'])
@require_user
def teams():
	return render_template('dashboard/teams.html', own_teams=g.user.get_teams())

@dashboard.route('/team/<int:tid>')
@require_user
def team(tid):
	return render_template('dashboard/team.html', team=Team.from_id(tid))