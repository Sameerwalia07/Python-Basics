arr1 = [1, 5, 10, 20, 40, 80]
arr2 = [6, 7, 20, 80, 100]
arr3 = [3, 4, 15, 20, 30, 70, 80, 120]


#typecasting into sets

set1 = set(arr1)
set2 = set(arr2)
set3 = set(arr3)

#join using intersection 

set4 = set1.intersection(set2)

set5 = set4.intersection(set3)

set5 = list(set5)

print(set5)





