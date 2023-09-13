''' 
Write a program to print the following matrix pattern
(increasing prime numbers from the centre toward the
boundaries) using generic controls over print. You are not
allowed to use any auxiliary space to keep the matrix. Let the
line number be user input. E.g., for an input of 9 the program
will return the following output.
7 7 7 7 7 7 7 7 7
7 5 5 5 5 5 5 5 7
7 5 3 3 3 3 3 5 7
7 5 3 2 2 2 3 5 7
7 5 3 2 1 2 3 5 7
7 5 3 2 2 2 3 5 7
7 5 3 3 3 3 3 5 7
7 5 5 5 5 5 5 5 7
7 7 7 7 7 7 7 7 7
'''

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def generate_matrix_pattern(line_number):
    if line_number % 2 == 0:
        line_number += 1  # Ensure an odd line number

    center = line_number // 2
    matrix = []

    for i in range(line_number):
        row = []
        for j in range(line_number):
            distance = max(abs(center - i), abs(center - j))
            prime = center - distance + 1
            row.append(str(prime) if is_prime(prime) else ' ')
        matrix.append(row)
    for row in matrix:
        print(' '.join(row))

# User input
line_number = int(input("Enter the line number: "))
generate_matrix_pattern(line_number)
