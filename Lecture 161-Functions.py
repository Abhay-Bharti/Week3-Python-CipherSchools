# Function to return average of numbers

def average_finder(*args):
    avg = []
    for pair in zip(*args):
        avg.append(sum(pair)/len(pair))
    return avg

print(average_finder([1,5,9],[3,1,6],[7,5,2],[3,2,4]))

# Function using lambda expression

average_find = lambda *args : [ sum(pair)/len(pair) for pair in zip(*args) ]

print(average_find([1,5,9],[3,1,6],[7,5,2],[3,2,4]))