# Making a list with cubic numbers using list comprehension

cube = [i**3 for i in range(1,11)]
print(cube)

# Making a list with first character of another list'element

fruits = ['Apples', "Mango", 'Banana', 'Papaya']
char = [i[0] for i in fruits]
print(char)