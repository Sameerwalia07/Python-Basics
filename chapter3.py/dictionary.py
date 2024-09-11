#creating a dictionary

'''phones = {
    "John" : 9876543,
    "Anchal" : 1234567, 
    "Ashish" : 90145789,
    "Sameer" : 78765342
    
}
print(phones)

#checking type

print(type(phones))

#checking length

print(len(phones))

#accessing item

print(phones["John"])
print(phones.get("John"))

#if we want to print only keys
print(phones.keys())

#updating values

phones["John"] = 9816189
print(phones)


#add elements 
phones["Kia"] = 456789
print(phones)

#adding sequence
more_phones = {
    "Golu" : 7654321
}
phones.update(more_phones)
print(phones)

phones.popitem()   #this will remove last item 
print(phones)

#phones.clear()    #this will clear the dictionary
# print(phones)


#printing values
for x in phones.items():
    print(x)'''
    
    
#nested dictionaries
phones = {
    "Area1" : {
        "x" : 1,
        "y" : 2,
        "z" : 3
    },
    "Area2" : {
        "a" : 4,
        "b" : 5,
        "c" : 6 
    }
}
print(phones["Area1"]["x"])

