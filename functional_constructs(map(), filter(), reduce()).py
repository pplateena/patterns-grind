from functools import reduce


def square(x):
    return x * x

def add(x, y):
    return x + y

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(add, numbers)
print(sum_of_numbers)  # Output: 15

squared_numbers = list(map(square, numbers))
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]

even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4]