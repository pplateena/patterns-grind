def cube_generator(number):
    for i in range(1, number + 1):
        yield i ** 3


k = int(input("Enter range to be cubed"))

cubes = cube_generator(k)

print("generated this: \n", cubes)

for number in cubes:
    print(number)
