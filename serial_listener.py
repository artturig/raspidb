import serial
import sys
import MySQLdb

try:
    from configparser import ConfigParser
except ImportError:
    from ConfigParser import ConfigParser  # ver. < 3.0

config = ConfigParser()  # instantiate
config.read('mysql.config.ini')  # parse existing file
# read values from a mysql.config.ini
myhost = config.get('mysql', 'host')
myuser = config.get('mysql', 'user')
mypasswd = config.get('mysql', 'passwd')
mydb = config.get('mysql', 'db')

# check that we  have usb connected
try:
    serialport = serial.Serial("/dev/ttyUSB0", 57600, timeout=0.5)
except Exception, e:
    print >> sys.stderr, "Exception: %s" % str(e)
    print >> sys.stderr, "No valid usb found from dev"
    sys.exit(1)

# use config settings to db connection
db = MySQLdb.Connect(host=myhost,  # your host, usually localhost
                     user=myuser,  # your username
                     passwd=mypasswd,  # your password
                     db=mydb)  # name of the data base

cur = db.cursor()

# loop
while True:
    command = serialport.readline()
    print command
    s = command.strip()
    suffix = ";"
    if s.endswith(suffix) == False:  # in line is not ending with ; forget it
         x = "x" # do nothing
    elif not s:  # if s is empty forget it
        print "tyhja"
    else:
        s = s[:-1]  # remove tailing ;
        node, value = s.split(":")  # split message and assing variables
        if node == '1Node':
          cur.execute("INSERT INTO lampo1 (node, lampo)  VALUES (%s, %s) ", (node, value))
          db.commit()
        else:
          cur.execute("INSERT INTO rele1 (node, tila)  VALUES (%s, %s) ", (node, value))
          db.commit()

