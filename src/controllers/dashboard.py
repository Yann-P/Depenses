from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *
from models.Team import Team
from models.User import User
from models.Expenditure import Expenditure

from utils.middleware import *
import sys


dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/', methods=["get"])
@require_user
def index():
	return render_template('dashboard/index.html', own_expenditures=Expenditure.get_for_user(g.user.id))

@dashboard.route('/teams', methods=['get'])
@require_user
def teams():
	return render_template('dashboard/teams.html', own_teams=g.user.get_teams())

@dashboard.route('/team/<int:tid>', methods=['get'])
@require_user
def team(tid):
	return render_template('dashboard/team.html', team=Team.from_id(tid), team_expenditures=Expenditure.get_for_team(tid))

@dashboard.route('/team/<int:tid>/add_expenditure', methods=['post'])
@require_user
def add_expenditure(tid):
	who_paid = request.form.get('who_paid')
	amount = request.form.get('amount')
	title = request.form.get('title')
	comment = request.form.get('comment')
	Expenditure.insert(team_id=tid, user_id=who_paid, amount=amount, title=title, comment=comment)
	return redirect(url_for('dashboard.team', tid=tid))