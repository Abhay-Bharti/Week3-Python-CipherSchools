# Methods to make a dictionary

d = {}
d = dict()

# Methods to add data in a dictionary

d["name"] = "Abhay"
d["age"] = 25

l = {1: "a", 2 : "b"}
d.update(l)

# Methods to access a dictionary

print(d["name"])

print(d.keys()) #print all the keys
print(d.values()) #print all the values
print(d.items()) #print all the items

# Methods to iterate over a dictionary

for key, value in d.items():
    print(key,value)

# in keyword in dictionary

if 1 in d:
    print("True")

d.get('name')
d.get(4)

# Methods to delete data in dictionary

d.pop(2)
print(d)

d.popitem()
print(d) # delete last key value pair 