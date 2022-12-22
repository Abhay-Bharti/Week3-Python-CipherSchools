# Function to print a list of integer and floating numbers using list comprehension

def numbers(l):
    num = [i for i in l if type(i)==int or type(i)==float]
    return num

l = [True,False,[2,5,7],1,3.4,6,70]
print(numbers(l))