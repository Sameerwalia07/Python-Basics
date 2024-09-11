def outer_function():
    x=1    #variable in outer function
    
    def inner_function():
        y=3     #variable in inner function   
        result = x+y
        return result
    
    return inner_function()

output = outer_function()

print(output)