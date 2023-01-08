# Practice question 

from functools import wraps

def print_function_data(any_func):
    @wraps(any_func)
    def wrap(*args, **kwargs):
        print("You are calling subtract function.")
        return any_func(*args, **kwargs)
    return wrap

@print_function_data
def subtract(a,b):
    '''This function takes two numbers as parametres and give their difference'''
    return b - a

print("Differnce between two numbers is:",subtract(2,9))