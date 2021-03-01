from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
import math
from sklearn import svm
from sklearn import metrics

digits = datasets.load_digits()
print(dir(digits))
# print(digits.data.shape)
# print(digits.data.shape)
# print(digits.data)
# print(digits.target)
# print(digits.data[0])

# plt.matshow(digits.images[0] , cmap="Greys")
# plt.show()

# print(digits.target[0])

n_train = len(digits.data)*2//3
x_train = digits.data[:n_train]
y_train = digits.target[:n_train]
x_test = digits.data[n_train:]
y_test = digits.target[n_train:]

clf = svm.SVC(gamma=0.001)
clf.fit(x_train,y_train)
print(clf.score(x_test,y_test))

predicted = clf.predict(x_test)
print((y_test != predicted).sum())

print(metrics.classification_report(y_test,predicted))

print(metrics.confusion_matrix(y_test,predicted))

imgs_yt_preds = list(zip(digits.images[n_train:],y_test,predicted))
for index,(image,y_t,pred) in enumerate(imgs_yt_preds[404:416]):
    plt.subplot(3,4,index + 1)
    plt.axis('off')
    plt.tight_layout()
    plt.imshow(image,cmap="Greys",interpolation="nearest")
    plt.title(f'{y_t} pre:{pred}',fontsize=12)
    
plt.show()


