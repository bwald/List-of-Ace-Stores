#!/usr/bin/env python
import csv, sys, getopt, os
import sqlite3
import mechanize

class store:
	def __init__(self, snum, sname, sadd1, sadd2, scity, sstate, zcode):
		self.num = snum
		self.name = sname
		self.add1 = sadd1
		self.add2 = sadd2
		self.city = scity
		self.state = sstate
		self.zipcode = zcode

def addStores(z, c, br):
#	br.select_form(name = "frm")
#	br["fldAddress"] = z
	#for form in br.forms():
	#	print form 
	#addToDatabase(c, "123 fake street")
	estore = store(123, "test", "123 fake street", "building b", "springfield", "mass", 33313)
	print estore.num 
	print estore.name
	addToDatabase(c, estore)

def addToDatabase(c, examplestore):
	#c.execute("insert into storelist values (?, ?, ?, ?, ?, ?, ?)", (examplestore.num, examplestore.name, examplestore.add1, examplestore.add2, examplestore.city, examplestore.state, examplestore.zipcode))
	try:
		#c.execute("insert into storelist values (123, 'test', '123 fake street', 'building b', 'springfield', 'mass', '31323')")
		c.execute("insert into storelist values (?, ?, ?, ?, ?, ?, ?)", (examplestore.num, examplestore.name, examplestore.add1, examplestore.add2, examplestore.city, examplestore.state, examplestore.zipcode))
		print "we created it?"
	except:
		print "the tuple already existed"

	t = (123,)
	c.execute('select state from storelist where num=?', t)

	print c.fetchone()

	#for row in c:
	#	print row

def printZips(ziplist):
	for row in ziplist:
		print row

def main():
	# read list of zip codes
	zips = []
	zipReader = csv.reader(open('zips.txt', 'r'))
	for row in zipReader:
		zips.append(row[1]) 

	# check if database already exists and initialize it if necessary
	dbexisted = False
	if os.path.isfile('/tmp/ace-db'):
		dbexisted = True
	con = sqlite3.connect('/tmp/ace-db')
	curs = con.cursor()
	if not dbexisted:
		curs.execute('''create table storelist
			(num integer primary key, name text, add1 text, add2 text, city text, state text, zip integer)''')

	# initialize browser object
	browser = mechanize.Browser()
	browser.open("http://www.acehardware.com/mystore/storeLocator.jsp")

	# for each zip code add the stores nearest it to the database
	'''
	for zipcode in zips:
		addStores(zipcode, curs, browser)
		'''
	addStores(zips[1], curs, browser)

if __name__ == "__main__":
	sys.exit(main())
