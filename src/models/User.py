from models.db import *
from models.Expenditure import Expenditure
from models.Team import *
from werkzeug import check_password_hash, generate_password_hash

class User:

	def __init__(self, id, name, password_hash):
		self.id = id
		self.name = name
		self.password_hash = password_hash

	def get_expenditures(self):
		sql = """SELECT id, user_id, amount, date, title, comment, team_id
				 FROM expenditure 
				 WHERE user_id=%s"""
		res = query_fetch_all(sql, (self.id,))
		ret = []
		for row in res:
			ret.append(Expenditure(row['id'], row['user_id'], row['amount'], row['date'], row['title'], row['comment'], row['team_id']))
		return ret

	def get_teams(self):
		ret = []
		sql = """SELECT team_id AS tid 
				 FROM users_by_teams
				 WHERE user_id=%s"""
		res = query_fetch_all(sql, (int(self.id),))
		for row in res:
			ret.append(Team.from_id(row['tid']))
		return ret


	@staticmethod
	def from_id(id):
		res = query_fetch_one("SELECT id, name, password FROM user WHERE id=%s", (int(id),))
		if res is None:
			return None
		return User(res['id'], res['name'], res['password'])

	@staticmethod
	def login(name, password):
		sql = "SELECT id, password FROM user WHERE name=%s";
		cur = cursor()
		cur.execute(sql, (name,))
		res = cur.fetchone()
		ret = -1
		if cur.rowcount == 1 and check_password_hash(res['password'], password):
			ret = int(res['id'])
		cur.close()
		return ret


	@staticmethod
	def insert(name, password):
		sql = "INSERT INTO user (id, name, password) VALUES(NULL,%s,%s);";

		hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
		cur = cursor()
		cur.execute(sql, (name, hashed_password))
		uid = cur.lastrowid
		cur.close()
		return uid

	@staticmethod
	def exists(name):
		return 0 != num_rows("SELECT id FROM user WHERE name=%s", (name,))