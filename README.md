# raspidb
Listen serial and write to mysql db using python

Raspi_nrf.tzz

Create local file db_conf.py and insert following:

 --------------------------------------------------------------------------
import MySQLdb

def dbconn():
	db = MySQLdb.Connect(host="localhost", # your host, usually localhost
        user="root", # your username
        passwd="password", # your password
        db="raspi") # name of the data base

dbconn()
 --------------------------------------------------------------------------
