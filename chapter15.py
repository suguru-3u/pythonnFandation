import numpy as np

# a = np.array([1,2,3])
# print(a.dtype)

# data = (1,2,3)
# b = np.array(data,dtype=str)
# print(b.dtype)

# 

# data = [1,2,3]
# a = np.array(data).reshape(3,1)
# print(a)
# o = np.append(a,[[5]],axis = 0)
# o = np.insert(a,1,99)
# print(o)

# a.ravel()
# print(a.shape)
# print(len(a))
# print(a.size)

# c = np.append(a,[5,7,8])
# print(c)

# data = [10,20,30,40,50,60]
# a = np.array(data).reshape(2,3)
# print(a[:1,])
# b = a[:1,].astype(str)
# print(b)

# for i,item in np.ndenumerate(a):
#     print(i,item > 20)

# print(a[(a > 20) & (a < 40)])

# a = np.sort([3,1,4,1,4,5,6,7,8,8,9,3,4,6,7,8])[::-1]
# a[a%2 == 0] = 0
# print(a)
# a[a%2 == 1] = 1
# print(a)

# print(a)

# a = np.array([10,20,30,40,50,60]).reshape(2,3)
# print(a)
# b = a + 5
# print(b)
# print(b.sum(1))


sigma = 3.5
mu = 65

data = sigma * np.random.randn(200) + mu
x = float(input("得点は?"))
t_socre = 10 *(x - data.mean() / data.std() + 50)
print(round(data.mean(),1))
print(round(data.std(),1))
print(round(t_socre,1))