# Enumerate function to print index of string in list if available else print -1

def stringinlist(l, word):
    for i,name in enumerate(l):
        if name == word:
            return i
    return -1

l = ['Abhay', "Rohit", "Kavya", "Aradhna"]
word = input("Enter word to find: ")

print(stringinlist(l, word))