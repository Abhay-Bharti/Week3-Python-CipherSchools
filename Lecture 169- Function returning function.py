# Function inside function

def outer_func():
    def inside_func():
        print("Hello World")
    return inside_func


var = outer_func()
var()

def outer_func(name):
    def inside_func():
        print(f"Hi! My name is {name}.")
    return inside_func()

outer_func('Abhay Bharti')