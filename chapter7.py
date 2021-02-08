"""
 = (1,2),(3,4)
b = (5,6)
b += 9,
print(a + b)

week = tuple("日月火水木金土")
print(week)

data = (1,2,3,4,5,6,7,8,9)
top = data[::2]
print(top)

for i,item in enumerate(data,1):
    print(i,item)

(g,h) = 10,20
print(g)
print(h)
"""
"""
number = (4,8,12,16,20,24,28,32)
num = int(input("受験番号を入力してください"))
if num in number:
    print("合格")
else:
    print("不合格")
"""
"""
x = [1,2,3]
y = [4,5,6]
z = [7,8,9]
zzz = zip(x,y,z)
xyz = list(zzz)
print(xyz)

color_set = {"bule","pink","red","white","yellow"}
print(len(color_set))

num2 = set(range(0,20,2))
print(num2)
"""

fruite = set()
fruite.add("apple")
fruite.add("apple")
print(fruite)
fruite.remove("apple")
print(fruite)
