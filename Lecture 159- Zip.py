# zip function

user_id = ['user1', 'user2', 'user3']
name = ['mohit', 'paras', 'rititk']
last_name = ['sharma', 'mehta', 'kohli']

l = list(zip(user_id,name))
print(l)

list1 = list(zip(user_id, name, last_name))
print(list1)

d = dict(zip(user_id, name))
print(d)