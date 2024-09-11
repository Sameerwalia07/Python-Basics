number = int(input("Enter a positive number ="))

if number % 15 == 0:
    print("number is divisible by 15")
    
else:
    if number % 3 == 0 or number % 5 == 0 :
        print("number is not divisible by 15 but divisible by 3 or 5")
        
    else: 
        print("number is neither divisible by 3 nor 5")