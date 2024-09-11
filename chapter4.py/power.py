'''a=2
b=3
power=a**b
print("The exponentiation is:", power)'''


def power_a_b(a, b):
    
    #base case
    if b==0:
        return 1
    
    #recursive case
    ans=a*power_a_b(a, b-1)
    return ans

a=int(input("Enter a number a:"))
b=int(input("Enter a number b:"))

print(power_a_b(a, b))
    