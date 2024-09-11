input_tuple = (1, 2, 3, 4, 5, 6, 7)

list = []          #as tuples are immutable, so we have to change tuples into list

# adding values of tuples in list
for x in reversed(input_tuple):
    list.append(x)
    
output_tuple = tuple(list)   #typecast into tuple

print(output_tuple)





input_names = ("Sameer", "Anchal", "Ashish", "Ekta")

list = []

for x in reversed(input_names):
    list.append(x)
        
output_names = tuple(list)
print(output_names)    

    