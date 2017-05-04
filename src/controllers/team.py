from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *
from models.Team import Team
from models.User import User
from models.Expenditure import Expenditure
from models.Reimbursement import Reimbursement

from utils.middleware import *
import sys


team = Blueprint('team', __name__, template_folder='templates')


@team.route('/', methods=["get"])
@require_user
def index():
	return render_template('dashboard/index.html', own_expenditures=Expenditure.get_for_user(g.user.id))


@team.route('/list', methods=['get'])
@require_user
def list():
	return render_template('dashboard/teams.html', own_teams=g.user.get_teams())


@team.route('/<int:tid>', methods=['get'])
@require_user
@current_user_belongs_to_team
def view(tid):
	team = Team.from_id(tid)
	if not team:
		abort(404)
	return render_template('dashboard/team.html', 
		team=team, 
		team_expenditures=Expenditure.get_for_team(tid),
		team_reimbursements=Reimbursement.get_for_team(tid))


@team.route('/<int:tid>/add_expenditure', methods=['post'])
@require_user
@current_user_belongs_to_team
def add_expenditure(tid):
	who_paid 	= request.form.get('who_paid')
	amount 		= float(request.form.get('amount') or 0)
	title 		= request.form.get('title')
	comment 	= request.form.get('comment')
	if amount > 0 and title:
		Expenditure.insert(team_id=tid, user_id=who_paid, amount=amount, title=title, comment=comment)
	return redirect(url_for('team.view', tid=tid))

@team.route('/<int:tid>/add_reimbursement', methods=['post'])
@require_user
@current_user_belongs_to_team
def add_reimbursement(tid):
	sender 		= request.form.get('sender')
	recipient 	= request.form.get('recipient')
	amount 		= float(request.form.get('amount') or 0)
	comment 	= request.form.get('comment')
	if amount > 0 and sender != recipient:
		Reimbursement.insert(from_user=sender, to_user=recipient, amount=amount, comment=comment, team_id=tid)
	return redirect(url_for('team.view', tid=tid))


@team.route('/<int:tid>/remove_expenditure', methods=['post'])
@require_user
@current_user_belongs_to_team
def remove_expenditure(tid):
	eid = request.form.get('eid')
	expenditure = Expenditure.from_id(eid)
	if expenditure and expenditure.team_id == tid:
		Expenditure.remove(eid)
	return redirect(url_for('team.view', tid=tid))


@team.route('/<int:tid>/add_user', methods=['post'])
@require_user
@current_user_belongs_to_team
def add_user(tid):
	user_name 	= request.form.get('user_name')
	user = User.from_name(user_name)
	if user:
		Team.from_id(tid).add_user(user.id)
	return redirect(url_for('team.view', tid=tid))


@team.route('/<int:tid>/remove_user/<int:uid>', methods=['get'])
@require_user
@current_user_belongs_to_team
def remove_user(tid, uid):
	team = Team.from_id(tid)
	users = team.get_users()
	if len(users) > 1:
		team.remove_user(uid)
		return redirect(url_for('team.view', tid=tid))
	return redirect(url_for('team.view', tid=tid))


@team.route('/add', methods=['post'])
@require_user
def add():
	name 		= request.form.get('name')
	description = request.form.get('description')
	if(Team.exists(name)):
		return redirect(url_for('team.list'), error_team_exists=True)

	team = Team.insert(name=name, description=description)
	team.add_user(g.user.id)
	return redirect(url_for('team.list'))