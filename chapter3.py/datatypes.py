#list datatypes

'''fruits = ["Apple", "Banana", "Peaches", "Mango"]    #create a list
print(fruits)     #printing a list
print(type(list))     #type of list
print(len(fruits))       #length of list

if "Apple" in fruits:
    print("Apple is present in the list")
    
if "Mango" not in fruits:
    print("Mango is not in list")


#indexing in list

print(fruits[1])
print(fruits[-4])

print(fruits[1:3])'''

#adding elements to list

#fruits = ["Apple", "Banana", "Peaches"]

#fruits.append("Strawberry")

#fruits.insert(0, "Mango")

#fruits2 = ["Mango", "Strawberry"]
#fruits.extend(fruits2)
#print(fruits)




#removing elements

'''fruits = ["Apple", "Banana", "Mango", "Orange"]
#fruits.remove("Orange")

fruits.pop(1)
print(fruits)'''



#changing / updating elements in list

'''fruits = ["Apple", "Banana", "Mango", "Orange"]
#fruits[1] = "Strawberry"

fruits[0:3]=["Strawberry", "Peaches", "Kiwi"]
print(fruits)'''



#sorting a list

'''fruits = ["Apple", "Banana", "Strawberry", "Mango", "Orange"]
#fruits.sort()  #by default in ascending manner

fruits.sort(reverse = True)
print(fruits)'''





'''fruits = ["Apple", "Banana", "Mango", "Kiwi"]
new_fruits = [fruit for fruit in fruits if "a" in fruit]
print(new_fruits)'''

#new_fruits = fruits + new_fruits
#print(new_fruits)


#nested lists

fruits = ["Apple", "Banana", ["Mango", "Kiwi"], "Orange"]
print(fruits[2])
print(fruits[2][1])