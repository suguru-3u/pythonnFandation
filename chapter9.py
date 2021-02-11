stock = {"s":7,"t":12,"p":11}
print(stock)

print(len(stock))

d = {(2011,"ab"):10,(2011,"ax"):12.5}
print(d)

data = dict([("yellow",3),("bule",6),("green",5)])
print(data)

key = ["yellow","a","c"]
value = [3,6,5]
data2 = dict(zip(key,value))
print(data2)

data3 = dict(y = 3,b = 6,g = 5)
print(data3)

ssstock = dict.fromkeys(["s","n","m"],0)
print(ssstock)

aaaaa = {"yellow":3,"nule":3,"green":5}
aaaaa.setdefault("bule",10)
print(aaaaa)