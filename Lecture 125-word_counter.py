# Function to store character and their count in a dictionary

def word_counter(string):
    count = {}
    for i in string:
        count[i] = string.count(i)
    return count

string = input("Enter string: ")
print(word_counter(string))