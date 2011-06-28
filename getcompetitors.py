import csv

zipReader = csv.reader(open('zips.txt', 'r'))

zips = []

for row in zipReader:
	zips.add(row[1])

print zips
