#Aim:Write a program to perform transpose of a matrix.
# Branch: Comps
# Year: SE
# Sem: IV
# Subject: Python
# Name: Sidra Shaikh
# UIN: 231P064
# Roll No: 40
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[matrix[j][i] for j in range(rows)] for i in range(cols)]
    return transposed

# Function to take matrix input
def input_matrix(rows, cols):
    print(f"Enter elements for a {rows}x{cols} matrix:")
    return [[int(input(f"Element [{i+1}][{j+1}]: ")) for j in range(cols)] for i in range(rows)]

# Taking input from user
rows = int(input("Enter number of rows for the matrix: "))
cols = int(input("Enter number of columns for the matrix: "))
matrix = input_matrix(rows, cols)

# Compute transpose
transposed_matrix = transpose_matrix(matrix)

# Display result
print("Transposed Matrix:")
for row in transposed_matrix:
    print(row)
