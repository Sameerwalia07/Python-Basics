number1 = int(input("Enter 1st number:"))
number2 = int(input("Enter 2nd number:"))
number3 = int(input("Enter 3rd number:"))
 
'''if number1 > number2 and number1 > number3 :
    print("1st number is the largest")
    
elif number2 > number1 and number2 > number3 :
    print("2nd number is the largest")
    
else:
    print("3rd number is the largest")'''
    
    
if number1 > number2:
    if number1 > number3:
        print("number1 is greatest")
        
    else:
        print("number3 is greatest")
        
else: 
    if number2 > number3:
        print("number2 is greatest")
        
    else:
        print("number3 is greatest")