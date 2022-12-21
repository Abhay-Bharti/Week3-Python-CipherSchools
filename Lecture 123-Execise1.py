# Function to print a dictionary of numbers and its cube

def cube_finder(n):
    d = {}
    for i in range(1,n+1):
        d[i] = i**3
    return d

n = int(input("Enter Number: "))
print(cube_finder(n))