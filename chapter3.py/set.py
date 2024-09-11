#creating a set
names = {"Anchal", "Sameer", "Ashish"}

#printing sets
print(names)
print(len(names))

#check datatype
print(type(names))

#accessing the values of items
for x in names:
    print(x)
    
 #checking the items of list   
if "Anchal" in names:
    print("Anchal is present in the names!!")
    
if "Ekta" not in names:
    print("Ekta is not present in names!!")
    
    
#adding elements

names.add("Ekta")
print(names)


#adding another sequence in set           using update function
'''names_list = {"Ria", "Sia"}
names.update(names_list)
print(names)'''



#removing element from set              using remove function

#names.remove("Ria")
#print(names)

names.discard("Mia") #using discard fuction not gives an error for removing any element that is not present in the sequence
print(names)



#joining 2 sets

names_list = {"Ria", "Sia"} 
names_list2 = {"Hema", "Sia"}
names_list.union(names_list2)
print(names_list, names_list2) 

names_list3 = names_list.union(names_list2)
print(names_list3)

#keep only duplicates while joining
names_list.intersection_update(names_list2)
print(names_list)

#keep all values except duplicate
names_list.symmetric_difference_update(names_list2)
print(names_list)


  