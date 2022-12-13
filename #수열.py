#수열
print (list(range(10)))
print (list(range(2000, 2023)))

print ("---리스트 컴프리헨션---")
lst = list (range(1,11))
print([i**2 for i in lst if i>5])
lst2=[i**2 for i in lst if i>5]
print(lst2)
lst3=[]
for i in lst:
    if i>5:
        lst3.append(i**2)
print(lst3)

print ("--필터링--")
#함수 정의
def getBiggerThan20(i):
    return i>20

lst = [10,25,30]
iterL=filter (getBiggerThan20, lst)
for item in iterL:
    print(item)



