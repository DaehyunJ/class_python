#반복문
#DemoDictionary.py
import os
os.system("cls")

print("---구구단 출력---")
for x in [2,3,4,5,6]:
    print ("---{0}단---".format(x))
    for y in [1,2,3,4,5,6,7,8,9]:
        print("{0} * {1} = {2}".format(x,y,x*y))

print ("---break---")
list= [1,2,3,4,5,6,7,8,9,10]
for i in list:
    #추가 탈출조건
    if i>5:
        break
    print(i)
    

    
        