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

x = range(0,360)
y = [math.sin(math.radians(d)) for d in x]
plt.plot(x,y)
plt.show()