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

	file_name = "CS2300P1aAmos.out"+matrix[0]

	with open(file_name,"w") as file:
		

	while row_start < matrix_row*matrix_column:
		print(matrix_values[row_start:row_end])
		row_start+=matrix_column
		row_end+=matrix_column

print_and_write("Amatrix")
print_and_write("Bmatrix")