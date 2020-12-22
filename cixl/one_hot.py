import pyprind
import pandas as pd
import os
from nltk.corpus import stopwords
import re
import numpy as np
from sklearn.model_selection import KFold
from gensim.models.word2vec import Word2Vec
import jieba
import joblib
from sklearn.svm import SVC
from sklearn.model_selection import  train_test_split
# a,b,c,d=train_test_split()

#创建一个数据集X和相应的标签y,X中样本数目为100
X, y = np.arange(200).reshape((100, 2)), range(100)
#用train_test_split函数划分出训练集和测试集，测试集占比0.33
X_train, X_test, y_train, y_test = train_test_split( X, y, test_size=0.33, random_state=42)

print("The length of original data X is:", X.shape[0])
print("The length of train Data is:", X_train.shape[0])
print("The length of test Data is:", X_test.shape[0])
print(X,y)