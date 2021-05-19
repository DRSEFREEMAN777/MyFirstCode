import csv

with open('data.csv','r') as csvfile:
	#reader can iterate over lines of csv file
	csvreader = csv.reader(csvfile)
	
	#reading first row of field names
	fields = csvreader.__next__()
	print('Field Names\n--------------')
	for field in fields:
		print("%8s"%field, end='')

	print('\nRows\n---------------------')	
	#reading rows
	for row in csvreader:
		#access and print each field value of row
		for col in row: 
			print("%8s"%col, end='')
		print('\n') 

# Read CSV File using For loop and String split use Python For Loop and Split String Operation to read csv file.

with open('data.csv') as fp:
	#field names
	print('Field Names\n--------------')
	fields = fp.readline()
	for field in fields.split(','):
		print("%8s"%field, end='')
	
	print('Rows\n---------------------')	
	#reading data rows
	for line in fp:
		chunks = line.split(',')
		for chunk in chunks:
			print("%8s"%chunk, end='')
