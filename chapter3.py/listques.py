'''n = int(input("Enter the size of list :"))

list = []

for _ in range(n):
    num = int(input())
    list.append(num)
    
idx1 = int(input("Enter first index number :"))
idx2 = int(input("Enter second index number :"))
print(list)

#swapping value at index1 and index2
 
temp = list[idx1]
list[idx1] = list[idx2] 
list[idx2] = temp

print(list)    '''


#2 question

n = int(input("Enter the size of list :"))

list = []

for _ in (n):
    fruits = input("")
    list.append(fruits)

idx1 = input("Enter the 1st index number: ")
idx2 = input("Enter the 2nd index number: ")

print(list)

#swapping the items

temp = list[idx1]    
list[idx1] = list[idx2]
list[idx2] = temp

print(list)