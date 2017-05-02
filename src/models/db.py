import MySQLdb

db = MySQLdb.connect(host="localhost",
    user="root",
    passwd="aaaaaa",
    db="depenses",
    autocommit=True)

def cursor():
	return db.cursor(cursorclass=MySQLdb.cursors.DictCursor)

def query(*args, **kwargs):
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