def fibbonaci(n):
    if n==1:  #base case
        return 0
    elif n==2:   #base case
        return 1
    
    else:   #recursive case
       return(fibbonaci(n-1)+fibbonaci(n-2))
   
   
   
n= int(input("Enter the value of n :"))
for i in range(1, n+1):
  print(fibbonaci(i)) 