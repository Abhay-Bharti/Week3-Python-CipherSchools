# More of zip function 

l1 = [1,2,3,4]
l2 = [5,6,7,8]

l3 = list(zip(l1,l2))
print(l3)

# To unpack the list

l4,l5 = zip(*l3)

print(l4)
print(l5)