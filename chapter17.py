from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import svm
from sklearn import metrics

# iris = datasets.load_iris()
# print(dir(iris))
# print(iris.DESCR)

# x = iris.data
# y = iris.target

# print(x)
# print(y)

# print(iris.feature_names)

# plt.scatter(x[:50,0],x[:50,1],color='r' ,marker='o',label='setosa')
# plt.scatter(x[50:100,0],x[50:100,1],color='g' ,marker='+',label='setosa')
# plt.scatter(x[100:,0],x[100:,1],color='b' ,marker='x',label='setosa')
# plt.title("Yes")
# plt.xlabel('sepal length(cm)')
# plt.ylabel('sepal width(cm)')
# plt.legend()
# plt.show()


#  plt.title("Yes")
# plt.xlabel('sepal length(cm)')
# plt.ylabel('sepal width(cm)')
# plt.legend()
# plt.show()


from time import sleep
from threading import Thread
# Threadオブジェクトをインポート
 
target_time = 10
 
def up_timer(secs):
    for i in range(0,secs):
        print(i)
        sleep(1)
    print("カウントアップ終了！")
 
 
def down_timer(secs):
    # for i in range(0,secs):から変更
    for i in range(secs, -1, -1):
        # 以下同じ・・・
 
        print(i)
        sleep(1)
    print("カウントダウン終了！")
 
# Threadインスタンスをタイマーごとに生成する
thread_1 = Thread(target=up_timer,args=(target_time,))
thread_2 = Thread(target=down_timer,args=(target_time,))
 
# それぞれのスレッドを起動する
thread_2.start()


plt.scatter(x[:50,0],x[:50,1],color='r' ,marker='o',label='setosa')
plt.scatter(x[50:100,0],x[50:100,1],color='g' ,marker='+',label='setosa')
plt.scatter(x[100:,0],x[100:,1],color='b' ,marker='x',label='setosa')
plt.title("Yes")
plt.xlabel('sepal length(cm)')
plt.ylabel('sepal width(cm)')
plt.legend()
plt.show()