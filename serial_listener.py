import serial
import MySQLdb
import sys
import db_conf

db_conf.dbconn()

# check that we  have usb connected
try:
	serialport = serial.Serial("/dev/ttyUSB0", 57600, timeout=0.5)
except Exception, e:
	print >> sys.stderr, "Exception: %s" % str(e)
	print >> sys.stderr, "No valid usb found from dev"
	sys.exit(1)

cur = db.cursor()

while True:    
	command = serialport.readline()
	print command
	s = command.strip()
#	s = s.replace(".", ",")

#	query = "SELECT lampo from valo1"
#	cur.execute(query)
#	ver = cur.fetchone()

#	print "luku on %s " % ver
#	query = "INSERT INTO valo1 SET lampo = 1"
	if not s:
		print "tyhja"
	else:	
		query = "INSERT INTO valo1 SET lampo = %s " % (s)
		print query
		cur.execute(query)
		db.commit()