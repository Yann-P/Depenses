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

	@staticmethod
	def from_id(id):
		sql = "SELECT id, name, description FROM team WHERE id=%s"
		res = query_fetch_one(sql, (int(id),))
		return Team(res['id'], res['name'], res['description'])