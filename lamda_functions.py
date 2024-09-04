
square = lambda x: x**2
cube = lambda x: x**3
# cute recursion
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)


basic_math = [square, cube, factorial]

for operation in basic_math:
    print(operation(3))