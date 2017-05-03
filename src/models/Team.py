from models.db import *


class Team:

	def __init__(self, id, name, description):
		self.id = id
		self.name = name
		self.description = description

	def get_users(self):
		from models.User import User
		ret = []
		sql = "SELECT user_id FROM users_by_teams WHERE team_id=%s"
		res = query_fetch_all(sql, (int(self.id),))
		for row in res:
			ret.append(User.from_id(row['user_id']))
		return ret

	def get_total_spent(self):
		sql = """SELECT SUM(amount) AS "sum"
				 FROM expenditure 
				 WHERE team_id=%s"""
		res = query_fetch_one(sql, (int(self.id),))
		return res['sum'] or 0

	def add_user(self, uid):
		sql = """INSERT INTO users_by_teams (id, user_id, team_id)
				 VALUES(NULL, %s, %s)"""
		cur = query(sql, (int(uid), int(self.id)))
		cur.close()


	@staticmethod
	def insert(name, description):
		sql = """INSERT INTO team (id, name, description)
				 VALUES(NULL, %s, %s);"""
		cur = cursor()
		cur.execute(sql, (name, description))
		tid = cur.lastrowid
		cur.close()
		return Team.from_id(tid)


	@staticmethod
	def from_id(id):
		sql = "SELECT id, name, description FROM team WHERE id=%s"
		res = query_fetch_one(sql, (int(id),))
		return Team(res['id'], res['name'], res['description'])

	@staticmethod
	def exists(name):
		return 0 != num_rows("SELECT id FROM user WHERE name=%s", (name,))