from flask import request, session, url_for, redirect, \
    render_template, abort, g, flash, Blueprint, jsonify

import MySQLdb
from models.db import *
from models.Team import Team
from models.User import User
from models.Expenditure import Expenditure
from models.Transaction import Transaction

from utils.middleware import *
import sys


dashboard = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard.route('/', methods=["get"])
@require_user
def index():
	total_sent = g.user.get_total_sent()
	total_received = g.user.get_total_received()
	transactions_balance = - total_sent + total_received
	total_spent = g.user.get_total_spent()
	balance = transactions_balance - total_spent

	return render_template('dashboard/index.html', 
		own_expenditures=Expenditure.get_for_user(g.user.id),
		own_transactions=Transaction.get_for_user(g.user.id),
		total_sent = total_sent,
		total_received = total_received,
		total_spent = total_spent,
		transactions_balance = transactions_balance,
		balance = balance)


@dashboard.route('/teams', methods=['get'])
@require_user
def teams():
	return render_template('dashboard/teams.html')