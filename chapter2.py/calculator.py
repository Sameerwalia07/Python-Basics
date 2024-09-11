num1 = int(input("Enter a number1 ="))
num2 = int(input("Enter a number2 ="))

operator = input("Enter operator")

match operator:
    case "+":
        print("The sum of numbers is", num1 + num2)
        
    case "-":
        print("The subtraction of numbers is", num1 - num2)
        
    case "/":
        print("The division of numbers is", num1 / num2)
        
    case "*":
        print("The multiplication if numbers is", num1 * num2)
        
    case _:
        print("Enter a valid operator")