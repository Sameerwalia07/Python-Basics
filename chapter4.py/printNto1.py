'''def print_n_to_1(n):
    
    #base case
    if n==0:
        return
    
    
    
    #recursive case
    print_n_to_1(n-1)
    print(n)
    return
print_n_to_1(7)'''

#sum of 1 to n numbers

def sum_of_1_to_n(n):
    #base case
    if n==1:
        return 1
    
    
    #recursive case
    ans = n + sum_of_1_to_n(n-1)
    return ans

#n=int(input("Enter a number :"))
print(sum_of_1_to_n(5))




    
    