#!/usr/bin/env python
import csv, sys, getopt, os
import sqlite3
import mechanize


def addStores(z, c, br):
#	br.select_form(name = "frm")
#	br["fldAddress"] = z
	#for form in br.forms():
	#	print form 
	addToDatabase(c, "123 fake street")

def addToDatabase(c, address):
	#c.execute("insert into storelist values (123, 'test', '123 fake street', 'building b', 'springfield', 'mass', '31323')")
	t = (123,)
	c.execute('select state from storelist where num=?', t)

	for row in c:
		print row

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
