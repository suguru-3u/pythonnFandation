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

"""
r = "23,45,6,7,89,99,22,22"
top = r.split(",",3)[:3]
print(top)

b = "and".join(r)
print(b)

colors = [1]
data = [2]
newdate = colors.extend(data)
print(newdate)

ccc = ["red","bule","geen","orenge","pink"]
print(ccc[:3])

letter = ["a","b","c","d","e","f","g","h"]
print(letter[::2])

print(letter[1:5][::2])

print(letter[::-1])

list_a = [1,2,3]
list_b = list_a
list_c = [1,2,3]

print(list_a == list_b)
print(list_a == list_c)

print(list_a is list_b)
print(list_a is list_c)

list_a.append(88)
print(list_a)
print(list_b)
list_b.append(55)
print(list_a)
print(list_b)

list_menber = [10,20,30,40,50]
list_work = list_menber.copy()
print(list_menber.reverse())
"""

numbers = [2,-3,4,-5,6]
sum = 0
for i,num in enumerate(numbers,2):
    print(f"{i}:",num)
    if num > 0:
        sum += num
print(sum)

nums = [numm *2 for numm in numbers]
print(nums)

print(2 in numbers)

id_list = ["1234","567","890","555","4432","6789"]
"""
while True:
    id = input("idを入力してください")
    if id == "q":
        print("終了")
        break
    try:
        pos = id_list.index(id)
        print(str(pos+1)+ "番目のメンバーです")
    except:
        print("メンバーはいません")
"""
print(id_list.count("1234"))