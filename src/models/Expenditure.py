from models.db import *

class Expenditure:

	def __init__(self, id, user_id, amount, date, title, comment, team_id):
		self.id = id
		self.user_id = user_id
		self.amount = amount
		self.date = date
		self.title = title
		self.comment = comment
		self.team_id = team_id

	@staticmethod
	def insert(user_id, amount, date, title, comment, team_id):
		sql = "INSERT INTO user (id, user_id, amount, date, title, comment, team_id) VALUES(NULL,%s,%s);";
		cur = cursor()
		cur.execute(sql, (user_id, amount, date, title, comment, team_id))
		eid = cur.lastrowid
		cur.close()
		return eid