import csv, sys, getopt



def printZips(ziplist):
	for row in ziplist:
		print row

def findStoresByZip(ziplist):
	



def main(argv=None):
	if argv is None:
		argv = sys.argv
	try:
		try:
			opts, args = getopt.getopt(argv[1:], "h", ["help"])
		except getopt.error, msg:
			raise Usage(msg)
	except Usage, err:
		print >>sys.stderr, err.msg
		print >>sys.stderr, "for help use --help"
		return 2

	zipReader = csv.reader(open('zips.txt', 'r'))

	zips = []

	for row in zipReader:
		zips.append(row[1]) 

	printZips(zips)

if __name__ == "__main__":
	sys.exit(main())
