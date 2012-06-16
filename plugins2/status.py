#!/usr/bin/python
# status.py - retrieve and display database server version

import sys
import MySQLdb

try:
	conn = MySQLdb.connect (host = "localhost", 
									user = "chris", 
									passwd = "sunnysar522", 
									db = "mvLocations")
except MySQLdb.Error, e:
     print "Error %d: %s" % (e.args[0], e.args[1])
     sys.exit (1)
     

from plugin import *
class status(Plugin):

    @register("en-US", "(zbox)|(zbox.* [a-z]+)")
    def test2(self, speech, language):
        global zbox
        if speech.lower() == 'zbox':
            self.say("Please specify a location number.")
        else:
            q = speech.split(' ',1)           				
			cursor = conn.cursor (MySQLdb.cursors.DictCursor)
			cursor.execute ("""
								SELECT *
								FROM location
								WHERE host = %s
								""", (q))
			result_set = cursor.fetchall ()
			for row in result_set:
					uptime = "%s" % (row["uptime"])							
			cursor.close ()					
			conn.commit ()
			conn.close ()
			self.say(uptime, None)
			self.complete_request ()