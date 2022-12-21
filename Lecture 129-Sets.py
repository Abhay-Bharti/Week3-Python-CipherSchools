# Set - unorderd collection of unique elements
# List and dictionary cannot be stored in a set


# Remove of duplicate
L = [1,1,2,3,4,5,5,5,6,7,7,7]
print(list(set(L)))

# Add data in set

s1 = {1,2,4,5,6,6.7,7}
s1.add(3)

# Delete data in set

s1.remove(3) # only works if 3 is availble in s1

s1.discard(0) # can work 0 is not available in s1 [no error occurs]

s1.clear() # delete all element in a set

# Copy Method

s2 = s1.copy()
print(s2)