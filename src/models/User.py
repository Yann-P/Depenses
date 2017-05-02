from models.db import *
from werkzeug import check_password_hash, generate_password_hash

class User:

	def __init__(self, id, name, password_hash):
		self.id = id
		self.name = name
		self.password_hash = password_hash

	@staticmethod
	def from_id(id):
		res = query_fetch_one("SELECT id, name, password FROM user WHERE id=%s", (id,))
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
			ret = (int)(res['id'])
		cur.close()
		return ret


	@staticmethod
	def insert(name, password):
		sql = "INSERT INTO user (id, name, password) VALUES(NULL,%s,%s);";

		hashed_password = generate_password_hash(password, method='pbkdf2:sha256')
		cur = cursor()
		cur.execute(sql, (name, hashed_password))
		res = cur.lastrowid
		cur.close()
		print ("insert name=%s pass=%s res=%s" % (name, hashed_password, res))
		return res

	@staticmethod
	def exists(name):
		return 0 != num_rows("SELECT id FROM user WHERE name=%s", (name,))