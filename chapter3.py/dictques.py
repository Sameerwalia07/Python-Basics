'''input = {
    "a" : 100,
    "b" : 200,
    "c" : 300
}

#sum = input["a"]+input["b"]+input["c"]   #done in basic way
#print("Sum of these inputs is: ", sum)


print('The sum of these values is :', sum(input.values()))'''


#Question : 2

#mirror operation

input_string = input("Enter a string: ")
n = int(input("Enter the value of n: "))

#creating dictionary

alphabets = "abcdefghijklmnopqrstuvwxyz"
reverse = alphabets[::-1]   #:: one denotes starting and other ending point of string and -1 is for right to left 
dict1 = dict(zip(alphabets, reverse))

#finding the part of string in which we have to do mirror operation

prefix = input_string[0:n-1]
suffix = input_string[n-1:]

#finding the mirror string

mirror = ""
for i in range(0, len(suffix)):
    mirror = mirror + dict1[suffix[i]]  #it means that from dict1 we will choose the reverse element and add it in mirror string
    
#creating final string
result = prefix + mirror
print("The result is: ", result)
    