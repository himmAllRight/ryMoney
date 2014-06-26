import csv

with open('transactionReg.csv', 'r') as trans:
	reader = csv.reader(trans)
	next(reader)

	for row in reader:
		print(row[0])