'''n = int(input("Enter a value of n :"))

for i in range (n) : #loop for rows
    for j in range (1, n+1) : #loop for columns
        print (j, end = "")
    print ()'''
    
    
#pattern 2

'''n = int(input("Enter a value of n :"))

for i in range (1, n+1):
    for j in range (1, i+1) :
        print (j, end = "")
        
    print()'''
    
    #pattern 3
    
'''n = int(input("Enter a value of n :"))

for i in range (65, n+1):
    for j in range (65, i+1):
        print(chr(j), end = "")
    print()'''
    

#pattern 4

n = int (input("Enter a value of n :"))
for i in range (1,n+1):
    #printing spaces
    print(" " * (n-i), end = "")
    
    #printing digits
    
    for j in range (1, 2 * i):
        print(j, end = "")
    print()
    
    
    
    