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

data = [10,20,30,40,50,60]
a = np.array(data).reshape(2,3)
print(a[0,1])