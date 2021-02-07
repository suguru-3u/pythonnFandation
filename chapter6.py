#nums = [1] *10
#print(nums)

"""
r101 = "佐藤"
r102 = "田中"
r103 = "鈴木"
r201 = "青木"
r202 = "広田"
r203 = "野村"
floor1 = [r101,r102,r103]
floor2 = [r201,r202,r203]
apartment = [floor1,floor2]
apartment[0][2] = "マイケル"
print(apartment)
print(len(apartment))
"""

"""
pos = int(input("取り出す位置"))
colors = ["red","bule","green","orenge"]

try:
    item = colors[pos]
    print(item)
except IndexError :
    print("インデックスエラー")
except Exception as error:
    print(error)
"""
"""
colors = ["red","bule","green","orenge"]
if colors:
    dessert = colors.pop()
    print(dessert)
print(colors)
"""

"""
colors = ["red","bule","green","orenge","bule"]
print("削除前",colors)
target = "bule"
while target in colors:
    colors.remove(target)
print("削除後",colors)
"""

r = "23,45,6,7,89,99,22,22"
top = r.split(",",3)[:3]
print(top)