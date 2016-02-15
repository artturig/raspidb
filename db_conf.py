import MySQLdb

def dbconn():
	db = MySQLdb.Connect(host="localhost", # your host, usually localhost
        user="root", # your username
        passwd="", # your password
        db="raspi") # name of the data base

dbconn()