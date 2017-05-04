from models.db import *
from models.User import User
from models.Team import Team
import time

class Reimbursement:

	def __init__(self, id, from_user, to_user, amount, comment, date, team_id):
		self.id = id
		self.from_user = from_user
		self.to_user = to_user
		self.amount = amount
		self.date = date
		self.comment = comment
		self.team_id = team_id

	def get_sender_user(self):
		return User.from_id(self.from_user)

	def get_recipient_user(self):
		return User.from_id(self.to_user)

	def get_team(self):
		return Team.from_id(self.team_id)


	@staticmethod
	def insert(from_user, to_user, amount, comment, team_id, date=None):
		sql = """INSERT INTO reimbursement (id, from_user, to_user, amount, comment, team_id, date)
				 VALUES(NULL, %s, %s, %s, %s, %s, %s);"""
		datetime = time.strftime('%Y-%m-%d %H:%M:%S')
		cur = query(sql, (int(from_user), int(to_user), float(amount), comment, int(team_id), datetime))
		cur.close()

	@staticmethod
	def from_id(id):
		sql =  """SELECT id, from_user, to_user, amount, comment, date, team_id
				 FROM reimbursement 
				 WHERE id=%s"""
		res = query_fetch_one(sql, (int(id),))
		if res is None:
			return None
		return Reimbursement.build(res)

	@staticmethod
	def remove(id):
		sql =  """DELETE FROM reimbursement WHERE id=%s"""
		cur = query(sql, (int(id),))
		cur.close()

	@staticmethod
	def build(row):
		return Reimbursement(row['id'], row['from_user'], row['to_user'], row['amount'], row['comment'], row['date'], row['team_id'])
