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

"""
name = ""
if not name:
    name = "匿名"
print(name)
"""

"""
count = 1
while count < 5:
    print(count)
    count += 1
"""

"""
from random import randint
t = 5
p = 0
f = "{:>4}"

while t > 0:
    v = randint(1,20)
    print(f.format(v))
    p += v
    t -= 1
    if p > 30:
        print("中断")
        break

print('-' * 4)
print(p)
"""
from random import randint
"""
miss = 0
correct = 0
print("問題!3回間違えたら終了,やめたくなったら「q」を押してね")

while miss < 3:
    a = randint(1,1000)
    b = randint(1,1000)
    ans = a + b
    question = f"問題!{a}+{b}はいくつですか?"
    value = input(question)
    if value == "q":
        break
    if value == str(ans):
        correct +=1
        print("正解!")
    else:
        miss += 1
        print("違います")

print('-' * 20)
print("正解:" ,correct)
print("間違い：",miss)
"""

"""
menber = []
while len(menber) < 10:
    n = randint(-10,100)
    if n < 0:
        print(f"中断:{n}")
        break
    if n in menber:
        print(f"同じ数字:{n}")
        continue
    menber.append(n)
else:
    print(menber)
"""

for i in range(10):
    print(i)

