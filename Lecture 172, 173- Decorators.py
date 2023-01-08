#  Decorators functions --> Enhances the functionality of the function

from functools import wraps

def decorator(any_func):
    @wraps(any_func)
    def wrap(*args,**kwargs):
        print("I am Charles Babbage, The father of computer")
        return any_func(*args, **kwargs)
    return wrap

@decorator
def add(a,b):
    '''Function to add numbers'''
    return a + b

print(add(5,3))
print(add.__doc__)
print(add.__name__)