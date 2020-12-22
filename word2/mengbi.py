import pandas as pd
import numpy as np
import jieba
import re
import tensorflow
import keras
from word2.chengguo import *
import ast
from sklearn.model_selection import train_test_split

train_x,test_x,train_y,test_y=train_test_split(sentences,file_data.label.values,test_size=0.1,random_state=0)
print(train_x)
print(train_y.shape,test_y.shape)
all_data=list(train_x)+list(test_x)
print(all_data)
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
tokenizer=Tokenizer() #分词器
tokenizer.fit_on_texts(all_data) #生成一个词典
sequences=tokenizer.texts_to_sequences(all_data)#将文档转换为向量
word_index=tokenizer.word_index
print(word_index.items())
