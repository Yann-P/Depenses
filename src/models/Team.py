from models.db import *
from utils.money_distribution import get_money_distribution

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

	def get_total_transactions_between(self, uid1, uid2):
		positive = query_fetch_one("SELECT SUM(amount) AS res FROM transaction WHERE from_user=%s AND to_user=%s AND team_id=%s", (int(uid1), int(uid2), int(self.id)))
		negative = query_fetch_one("SELECT SUM(amount) AS res FROM transaction WHERE to_user=%s AND from_user=%s AND team_id=%s", (int(uid1), int(uid2), int(self.id)))
		positive = float(positive['res'] or 0)
		negative = float(negative['res'] or 0)
		return - positive + negative

	def get_total_spent(self):
		sql = """SELECT SUM(amount) AS "sum"
				 FROM expenditure 
				 WHERE team_id=%s"""
		res = query_fetch_one(sql, (int(self.id),))
		return res['sum'] or 0

	def get_avg_spent(self):
		return self.get_total_spent() / len(self.get_users())

	def get_money_distribution(self):
		ret = []
		total_spent = self.get_total_spent()
		users = self.get_users()
		avg = total_spent / len(users)
		expenditures = [0] * len(users)
		for i in range(len(users)):
			expenditures[i] = users[i].get_total_spent(self.id) + users[i].get_total_sent(self.id) - users[i].get_total_received(self.id)

		distribution = get_money_distribution(expenditures)

		for i in range(len(distribution)):
			for j in range(len(distribution[i])):
				if distribution[i][j] > 0.005:
					ret.append({'from': users[i].name, 'to': users[j].name, 'amount': distribution[i][j]})
		return ret


	def add_user(self, uid):
		sql = """INSERT INTO users_by_teams (id, user_id, team_id)
				 VALUES(NULL, %s, %s)"""
		cur = query(sql, (int(uid), int(self.id)))
		cur.close()

	def remove_user(self, uid):
		sql = """DELETE FROM users_by_teams 
				 WHERE user_id=%s
				 AND team_id=%s"""
		cur = query(sql, (int(uid), int(self.id)))
		cur.close()

	def contains_user(self, uid):
		sql = "SELECT id FROM users_by_teams WHERE team_id=%s AND user_id=%s";
		cur = cursor()
		cur.execute(sql, (int(self.id), int(uid)))
		ret = (cur.rowcount == 1)
		cur.close()
		return ret


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
		if res is None:
			return None
		return Team(res['id'], res['name'], res['description'])

	@staticmethod
	def exists(name):
		return 0 != num_rows("SELECT id FROM team WHERE name=%s", (name,))