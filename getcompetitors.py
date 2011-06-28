import csv




def 

def main:

	zipReader = csv.reader(open('zips.txt', 'r'))

	zips = []

	for row in zipReader:
		zips.append(row[1]) 

if __name__ == "__main__":
	main()
