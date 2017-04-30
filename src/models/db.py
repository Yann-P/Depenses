import MySQLdb

db = MySQLdb.connect(host="localhost",
    user="root",
    passwd="aaaaaa",
    db="binarytracker")

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