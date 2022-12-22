# list comprehension with if statement

# Function to print a list of even numbers

def even(l):
    d = [i for i in l if i%2==0]
    return d

l = list(range(0,23))
print(even(l))