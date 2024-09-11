#creating a tuple

colours = ("red", "blue", "green")

#creating a single tuple, for creating a single tuple we have to use (,)
#also we can write tuple 

fruit = ("apple" ,)

print(colours)
print(fruit)

#checking length of tuple 

print(len(colours))

#accessing items in tuple

print(colours[1]) #positive indexing

print(colours[-1])  #negative indexing

print(colours[0:2])  #range indexing

print(colours[-1:])

print(colours[-2:])


#traversing the tuple

for i in (colours):
    print(i)
    

#concatenating

'''more_colours = ("yellow", "white")
colours = colours + more_colours

print(colours)'''



#unpacking tuples

colour1, colour2, colour3 = colours   #the numbere of elements in tuple, the number of new variables must be same 

print(colour1, colour2, colour3)