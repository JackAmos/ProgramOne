#Jack Amos
#CS2300-002
#9/21/2019
#Project 1


def print_and_write(matrix):

	with open(matrix,'r') as file:
		contents = file.read()

	matrix_values = [int(x) for x in contents.split()]

	matrix_row = matrix_values.pop(0)
	matrix_column = matrix_values.pop(0)

	row_start = 0
	row_end = matrix_column
		
	matrix_string = ""

	while row_start < matrix_row*matrix_column:
		matrix_string += str(matrix_values[row_start:row_end]) + "\n"
		row_start+=matrix_column
		row_end+=matrix_column

	matrix_string = matrix_string.replace(",","").replace("[","").replace("]","")
	print(matrix_string)

	matrix_string = str(matrix_row)+" "+str(matrix_column)+" "+matrix_string

	file_name = "CS2300P1aAmos.out"+matrix[0]

	with open(file_name,"w+") as file:
		file.write(matrix_string)


def subtract(matrix1,matrix2):
	
	with open(matrix1,'r') as file:
		contents = file.read()

	matrix_values1 = [int(x) for x in contents.split()]

	matrix_row = matrix_values1.pop(0)
	matrix_column = matrix_values1.pop(0)

	with open(matrix2,'r') as file:
		contents = file.read()

	matrix_values2 = [int(x) for x in contents.split()]

	matrix_row = matrix_values2.pop(0)
	matrix_column = matrix_values2.pop(0)

	index = 0
	matrix_sub = []

	for n in matrix_values1:
		matrix_sub.append(n - matrix_values2[index])
		index+=1

	row_start = 0
	row_end = matrix_column
	matrix_string = ""

	while row_start < matrix_row*matrix_column:
		matrix_string += str(matrix_sub[row_start:row_end]) + "\n"
		row_start+=matrix_column
		row_end+=matrix_column


	matrix_string = matrix_string.replace(",","").replace("[","").replace("]","")
	print(matrix_string)

	matrix_string = str(matrix_row)+" "+str(matrix_column)+" "+matrix_string

	with open("CS2300P1aAmos.calc","w+") as file:
		file.write(matrix_string)


def transpose(matrix):
	
	with open(matrix,'r') as file:
		contents = file.read()

	matrix_values = [int(x) for x in contents.split()]

	matrix_row = matrix_values.pop(0)
	matrix_column = matrix_values.pop(0)

	index = 0
	column_iterator = 1
	matrix_string = ""

	while column_iterator <= matrix_row:

		if index >= matrix_row*matrix_column:
			index = column_iterator
			column_iterator+=1
			matrix_string = matrix_string+"\n"
		else:
			matrix_string = matrix_string+" "+str(matrix_values[index])
			index+=matrix_column

	print(matrix_string)

	matrix_string = str(matrix_row)+" "+str(matrix_column)+matrix_string

	with open("CS2300P1aAmos.trans","w+") as file:
		file.write(matrix_string)





#calling functions
print_and_write("Amatrix")
print_and_write("Bmatrix")
subtract("Amatrix","Bmatrix")
transpose("CS2300P1aAmos.calc")



