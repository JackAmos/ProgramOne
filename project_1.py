#Jack Amos
#CS2300-002
#9/21/2019
#Project 1


with open("Amatrix",'r') as file:
	contents = file.read()

matrix_values = [int(x) for x in contents.split() if x.isdigit()]

matrix_row = matrix_values.pop(0)
matrix_column = matrix_values.pop(0)

print(matrix_row)
print(matrix_column)
print(matrix_values)