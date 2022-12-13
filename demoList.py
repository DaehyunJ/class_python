#DemoList.py
strA="python is a strong language."

print(strA)
print("length of it:")
print( len(strA))

print(strA[0:3])
print(strA[:3])
print(strA[-3:])
print(strA[3:5])
print(type(strA))

print("---list---")
colors = ["red","blue", "green"]
print (len(colors))
print (type(colors))
print (colors[0])
print (colors[0:1])
print (colors[0:2])
print (colors[-2:])
colors.append("grey")
print(colors)
colors.insert(0,"purple")
print(colors)

#카운트
print(colors.count("blue"))
print(colors.index("blue"))
colors.remove("blue")
print (colors)
colors.extend(["red","yellow","black"])
print (colors)
colors.insert(1,["red","yellow","black"])
print (colors)
print(colors.pop())
print (colors)

#Union
unionA={"a","b",1,2,3}
unionB={"a","c",1,2,4}
print(unionA.union(unionB))
print(unionA.difference(unionB))
print(unionA.intersection(unionB))

