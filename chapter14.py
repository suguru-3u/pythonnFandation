import matplotlib.pyplot as plt
import math

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

x = [100,200,300,400,500]
Y1 = [40,45,60,80,100]
Y2 = [34,55,77,88,99]
Y3 = [25,65,77,44,77]
plt.plot(x,Y1,marker = "o",linestyle="-",label = "Y1")
plt.plot(x,Y2,marker = "v",linestyle="--",label = "Y2")
plt.plot(x,Y3,marker = "d",linestyle="-.",label = "Y3")
plt.show()