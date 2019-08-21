import MySQLdb
import os
from MySQLdb import OperationalError



def connect():

	db = MySQLdb.connect(os.environ['DBHOST'],
	    user="root",
	    passwd=os.environ['DBPW'],
	    db="depenses",
            charset="utf8",
	    autocommit=True)
	return db



def cursor():
	return db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def query(*args, **kwargs):
	global db
	cur = cursor()
	try:
		cur.execute(*args, **kwargs)
	except OperationalError as e:
		db = connect()
		cur = cursor()
		cur.execute(*args, **kwargs)
	return cur

def query_fetch_all(*args, **kwargs):
	cur = query(*args, **kwargs)
	res = cur.fetchall()
	cur.close()
	return res

def query_fetch_one(*args, **kwargs):
	cur = query(*args, **kwargs)
	res = cur.fetchone()
	cur.close()
	return res

def num_rows(*args, **kwargs):
	cur = query(*args, **kwargs)
	res = cur.rowcount
	cur.close()
	return res

db = connect()

