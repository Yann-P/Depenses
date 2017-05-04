from models.db import *
from models.User import User
from models.Team import Team
import time

class Expenditure:

	def __init__(self, id, user_id, amount, date, title, comment, team_id):
		self.id = id
		self.user_id = user_id
		self.amount = amount
		self.date = date
		self.title = title
		self.comment = comment
		self.team_id = team_id

	def get_user(self):
		return User.from_id(self.user_id)

	def get_team(self):
		return Team.from_id(self.team_id)

	@staticmethod
	def get_for_team(tid):
		sql = """SELECT id, user_id, amount, date, title, comment, team_id
				 FROM expenditure 
				 WHERE team_id=%s
				 ORDER BY date DESC"""
		res = query_fetch_all(sql, (int(tid),))
		ret = []
		for row in res:
			ret.append(Expenditure.build(row))
		return ret


	@staticmethod
	def get_for_user(uid):
		sql = """SELECT id, user_id, amount, date, title, comment, team_id
				 FROM expenditure 
				 WHERE user_id=%s
				 ORDER BY date DESC"""
		res = query_fetch_all(sql, (uid,))
		ret = []
		for row in res:
			ret.append(Expenditure.build(row))
		return ret

	@staticmethod
	def insert(user_id, amount, comment, title, team_id, date=None):
		sql = """INSERT INTO expenditure (id, user_id, amount, date, comment, title, team_id)
				 VALUES(NULL, %s, %s, %s, %s, %s, %s);"""
		datetime = time.strftime('%Y-%m-%d %H:%M:%S')
		cur = query(sql, (int(user_id), float(amount), datetime, comment, title, int(team_id)))
		cur.close()

	@staticmethod
	def from_id(id):
		sql =  """SELECT id, user_id, amount, date, title, comment, team_id
				 FROM expenditure 
				 WHERE id=%s"""
		res = query_fetch_one(sql, (int(id),))
		if res is None:
			return None
		return Expenditure.build(res)

	@staticmethod
	def remove(id):
		sql =  """DELETE FROM expenditure WHERE id=%s"""
		cur = query(sql, (int(id),))
		cur.close()

	@staticmethod
	def build(row):
		return Expenditure(row['id'], row['user_id'], row['amount'], row['date'], row['title'], row['comment'], row['team_id'])
