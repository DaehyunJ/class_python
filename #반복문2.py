#반복문2
#DemoDictionary.py
import os
os.system("cls")

lst = [1,2,3,4,5]
print([i**2 for i in lst])
print(lst)

for j in lst:
    print("{0}".format(j**2))
