#  Decorators functions --> Enhances the functionality of the function


def decorator(any_func):
    def wrap():
        print("I am Charles Babbage, The father of computer")
        any_func()
    return wrap

@decorator
def func1():
    print("Hi I am computer.")
    
@decorator
def func2():
    print("I am most intelligent of all time.")

# var = decorator(func1)
# var()

# var1 = decorator(func2)
# var1()

func1()
func2()