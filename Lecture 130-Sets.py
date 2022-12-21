s = {'a', 'b', 'c'}

# in keyword to check exitence of a data in set

if 'a' in s:
    print("True")

# for loop

for i in s:
    print(i)

s1 = {1,2,3,4,5,2,3}
s2 = {3,4,8,9,0}

# Union of sets

union = s1 | s2
print(union)

# Intersection of sets

intersection = s1 & s2
print(intersection)