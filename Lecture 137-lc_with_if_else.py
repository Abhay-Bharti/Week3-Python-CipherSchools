# list comprehension with if else condition

l = list(range(9,34))

new_list = [i*2 if i%2==0 else -i for i in l]
print(new_list)