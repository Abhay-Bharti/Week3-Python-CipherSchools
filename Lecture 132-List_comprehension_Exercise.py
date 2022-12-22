# Function to return a list whose elements are reverse of another list element using list comprehension

def reverse(l):
    return [i[::-1] for i in l]

fruits = ['apple','mango','banana','grapes']
print(reverse(fruits))