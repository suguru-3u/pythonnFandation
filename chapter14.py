import matplotlib.pyplot as plt
import math
import numpy as np

# data = [2,2.3,4.1,5.3,2.2,4.6]
# xdata = [1,2,3,4,5,6]
# plt.plot(data,xdata)
# plt.show()

# price = [200,300,400,500,600]
# count = [31,29,25,28,26]
# plt.plot(price,count,marker="o")
# plt.title("count-price")
# plt.xlabel("price")
# plt.ylabel("count")
# plt.grid(True)
# plt.show()

# x = range(0,360)
# y = [math.sin(math.radians(d)) for d in x]
# c = [math.cos(math.radians(d)) for d in x]
# plt.plot(x,y)
# plt.plot(x,c)
# plt.show()

# x = [100,200,300,400,500]
# Y1 = [40,45,60,80,100]
# Y2 = [34,55,77,88,99]
# Y3 = [25,65,77,44,77]
# plt.plot(x,Y1,marker = "o",linestyle="-",label = "Y1")
# plt.plot(x,Y2,marker = "v",linestyle="--",label = "Y2")
# plt.plot(x,Y3,marker = "d",linestyle="-.",label = "Y3")
# plt.show()

# labels = ["A","B","C","D","E"]
# x_pos = range(0,5)
# V = [91,45,17,88,47]
# plt.bar(x_pos,V,tick_label = labels)
# plt.show()

# labels = ["Green","Red","Yellow","Bule","White"]
# x_pos = range(0,5)
# A = [33,44,55,66,77]
# B = [11,22,33,44,55]
# bar1 = plt.bar(x_pos,A,color="g")
# bar2 = plt.bar(x_pos,B,color="c",bottom = A)
# plt.xticks(x_pos,labels,rotation = "vertical")
# plt.legend((bar1,bar2),("man","women"),loc = "upper right")
# plt.show()

# x = [1,2,3,4,5,6,7,8,9,10]
# y = [11,22,33,44,55,66,77,88,99,100]
# plt.scatter(x,y)
# plt.show()

# X,Y = np.random.rand(100),np.random.rand(100)
# V = np.random.rand(100)
# plt.scatter(X,Y,marker = "o", s = 200,c = V,cmap="Blues",edgecolors = "b")
# plt.colorbar()
# plt.grid(True)
# plt.show()

# labels = ["E","D","C","B","A"]
# V = [17,25,47,14,6]
# ex = [0,0,0,0,0]
# plt.pie(V,explode = ex,labels = labels,autopct = '%1.1f%%',startangle = 90)
# plt.show()

x1,y1 = range(0,5),[61,88,99,11,23]
x2,y2 = range(0,5),[61,55,22,11,23]
labels = ["a","b","c","d","e"]
fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)
ax1 .bar(x1,y1,color="b",tick_label= labels)
ax1.set_title("dog")
ax2 = fig.add_subplot(1,2,2)
ax2 .bar(x2,y2,color="g",tick_label= labels)
ax2.set_title("cat")
plt.show()