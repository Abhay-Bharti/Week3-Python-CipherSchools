# Function to print True if given number is even else print False

iseven = lambda a : a%2 == 0 

# Calling function iseven

a = int(input("Enter number: "))
print("Given number",a,"is Even:",iseven(a))
print("Given number",a+3,"is Even:",iseven(a+3))

# Function to print "Even " if even else "Odd" for odd number

check = lambda a : "Even" if a % 2 == 0 else "Odd"

a = int(input("Enter number: " ))
print("Given number is",check(a))