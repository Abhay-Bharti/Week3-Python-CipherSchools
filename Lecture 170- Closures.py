# Function returning function (Closures) 

def pow(x):
    def calc_power(n):
        return n**x
    return calc_power

cube = pow(3)
print(cube(4))  

square = pow(2)
print(square(5))