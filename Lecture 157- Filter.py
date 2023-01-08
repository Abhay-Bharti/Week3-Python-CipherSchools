# filter function

def iseven(s):
    if s % 2 == 0:
        return s

numbers = [1,2,5,8,6,3,5,9,4,8]
even = filter(iseven, numbers)
print(list(even))

# filter function using lambda expression 

even1 = list(filter(lambda a:a%2== 0, numbers))
print(even1)

# using list comprehension

even2 = [i for i in numbers if i%2==0]
print(even2)