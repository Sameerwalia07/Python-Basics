def factorial(n):
    ans = 1
    #base case
    if n ==0:
        return 1
    
    
    #recursive case
    ans=n * factorial(n-1)
    
    return ans

n = int(input("Enter a number :"))
output=factorial(n)
print("The factorial of given number is:", output)
    
        