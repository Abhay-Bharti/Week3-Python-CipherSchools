# Code to give maximum and minimum word with respect to its lenghth

names = ['Rocky Bhai', 'Mohit', 'ab', 'z']

print("Word with maximum length is:",max(names, key = lambda item: len(item)))
print("Word with minimum length is:",min(names, key = lambda item: len(item)))

# Code to print name whose age is greatest

students = {
'Amrendra' : {'score':90, 'age':24},
'mohit' : {'score':75, 'age':19},
'rohit': {'score':76, 'age':23}
}

print("Student with greatest age is:",max(students, key = lambda item: students[item]['age']))

# Code to print name of student whose score is greatest

students2 = [
{'name':'Amrendra', 'score':90,'age':24},
{'name':'mohit', 'score':70, 'age':19},
{'name':'rohit', 'score':100, 'age':25}
]

print("Person with highest score is:",max(students2, key = lambda item: item.get('score'))['name'])