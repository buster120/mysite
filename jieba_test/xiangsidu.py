import pandas as pd
import numpy as np
import jieba
# a=pd.DataFrame({'one':[1,2,3,4],'two':[9,8,7,6]},index=['a','b','c','d',])
# # a.name='数据值'
# # a.index.name='索引列'
# # a.columns.name='柱号'
# print(a)
# # newb=a.columns.insert(3,'three')
# newc=a.reindex(columns=['one','two','three'],fill_value=200)
#
# newc.drop('one',axis=1,)
# # print(newc)
# # newd=newc.reindex(fill_value=300)
# # print(newd)
# # a.to_csv("D:/linshishuju/shuju1.csv",encoding='utf8')

# import csv
# file_data=pd.read_csv("D:/linshishuju/shuju1.csv",encoding='utf8')
# newb=file_data.columns.insert(3,'threed')
# newc=file_data.reindex(newb,fill_value=200)
# newc.to_csv("D:/linshishuju/shuju1.csv")

from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer,TfidfVectorizer

vectorizer = TfidfVectorizer()

