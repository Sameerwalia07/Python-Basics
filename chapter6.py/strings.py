
#creating strings

name1 = 'Sameer Walia'

name2 = "Ashish Walia"

name3 = '''Ekta 
Walia'''


print(name1,  name2, name3)

#indexing

print(name1[0])
print(name2[7])
print(name3[-4])

#traversing a string
#using for loop
#for i in name1:
 #   print(i)
    
#using list comprehension
'''list=[char for char in name1]
for i in list:
 print(i)'''
 

#length
print(len(name1))

#find char/substring in a list
print(name2.find('Wal'))


#slicing in string

print(name1[1:5])
print(name2[-5:])
print(name3[4:9])

 