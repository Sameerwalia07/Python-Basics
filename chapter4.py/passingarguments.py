#pass by value


def addOne (x):
    x=x+1
    print("Inside_function is:", x)
    
x=4
addOne(x)
print("outside function is :", x)


#pass by reference

def modifylist(lst):
    lst.append(4)
    print("Inside function :", lst)
    
lst = [1,2,3]
modifylist(lst)
print("Output function :", lst)
