"""
input_number = input("好きな数字を入力してください");
number = int(input_number)
if number == 1:
    print("1です。")
elif number ==2:
    print("2です")
else:
    print("1以外です")

print("終了")
"""

"""
from random import randint
size = randint(5,20)#5~20の数字の生成
weight = randint(20,40)#20~40の数字を生成

if size > 10 and weight >= 25:
    result = "合格"
else:
    result = "不合格"

text = f"サイズ{size},重量{weight}:{result}"
print(text) 
"""

name = ""
if not name:
    name = "匿名"
print(name)
