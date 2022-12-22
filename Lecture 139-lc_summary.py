# list comprehension summary

square = [i**2 for i in range(0,11)]
print(square)

even = [i for i in range(0,11) if i%2 == 0]
print(even)

# if else

l = ["Ankit",'Amit', 'Mohit', 'Mandy']
new_list = [i[1] if i[0]=='A' else i[-1] for i in l]
print(new_list)

# nested list

matrix = [[i for i in range(2)] for i in range(5)]
print(matrix)