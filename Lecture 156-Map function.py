# map function

numbers = [1,2,3,4,5,6]

def cube(a):
    return a**3

cube = list(map(cube,numbers))
print(cube)

# list comprehension

new_cube = [i**3 for i in numbers]
print(new_cube)

# using lambda function with map function

cube1 = list(map(lambda x:x**3,numbers))
print(cube1)