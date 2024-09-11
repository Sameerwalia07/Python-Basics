'''n = int(input("Enter the value of n :"))

sum = 0

for i in range(0, n+1):
    sum += i
    
print("The sum of numbers till n is :", sum)'''


#write a function that prints hello

'''def printhello():
    #body of function
    print("Hello World!!")
    
printhello()'''



#fuctions that takes 2 numbers as input and returns the sum

def add(n1, n2):
    sum = n1+n2
    return sum

#x = 2
#y = 7
#print("The sum of numbers is :", add(x, y))

#positional argument :  in this according to the positions the value of arguments is considered
#print("The sum of numbers is:", add(2, 3))


#keyword arguments (named arguments)
#print("The sum of numbers is :", add(n2=7, n1=4))


#default arguments : if we don't assign any value to the arguments it takes any default values







#add all numbers program
#arbitary arguments
def all_numbers(*args):      # *args function is used when we don't have particular number of values
    sum = 0
    for i in args:
        sum+=i
    return sum
        
#output=all_numbers(1,2,3,4,5,6,7,999,7665,45,65,456789)
#print("The sum is :", output)


def student_info(**kwargs):
    for x, y in kwargs.items():
        print(x, "is", y)
        
student_info(name="Sameer", age=20, city="Ludhiana")
student_info(name="Anchal", age=20, city="Ludhiana")

        
