import pandas as pd
import numpy as np
import jieba
import re

import ast
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer,TfidfVectorizer

file_data=pd.read_csv("D:/linshishuju/shuju.csv",encoding='utf8')
# file_data=file_data.tail(1000)
# file_data.index=range(len(file_data))
#print(file_data)
#file_data.duplicated()  #查找重复的元素，返回布尔型
# print(file_data[file_data.duplicated()]) #为空
#print(np.any(pd.isnull(file_data))) #判断是否有缺失值，any是或运算，存在为True则返回True

file_data["review"]=file_data["review"].str.strip() #删除两边的空白
#print(file_data["review"])

pattern='[0-9a-zA-Z]+|\n+|\s|(。|，|,|？|！|\+|-|\*|=|（|）|\(|\)|：|&|￥|\$|_|#|@|%|^|-|【|】|\?|⑧|；|;|~|●●」|～|·|—|…)'
for i in range(len(file_data)):
    file_data.review[i]=re.sub(pattern,'',[x for x in file_data.review][i]) #删除数字字母换行符以及指定的中文字符，空白符，其他符号
print(file_data)
print(type(file_data))

#print(file_data[file_data.duplicated()])  #发现有重复值
file_data.drop_duplicates(inplace=True)#删除重复词，直接对原数据改变
file_data.index=range(len(file_data)) #对索引重新定义
#print(file_data.head())

for i in range(len(file_data)):
    file_data.review[i]=jieba.lcut(str(file_data.review[i]),cut_all=False)
# file_data['process']=file_data['review'].apply(lambda x:' '.join([w for w in x if w not in stopwords]))
# print(type(file_data.review[0]))
# print(file_data)
with open('D:/linshishuju/stopwords-master/baidu_stopwords.txt', encoding="utf-8") as txt_file:
    stopwords=[str(line.rstrip()) for line in txt_file.readlines()]  #下面的写法和此行效果一样
    a=['很','都','还']
    stopwords=stopwords+a
    # stopwords=[]
    # for line in txt_file.readlines():
    #     stopwords.append(line.strip())
    #
    # print(stopwords)
file_data['process']=file_data['review'].apply(lambda x:' '.join([w for w in x if w not in stopwords]))  #str
file_data['list_process']=file_data['review'].apply(lambda x:[w for w in x if w not in stopwords])
file_data.to_csv("D:/linshishuju/shuju.csv",encoding='utf8')
print(file_data['list_process'])

# #统计词频
# words=[]
# for content in file_data['list_process']:
#     con=content
#     for i in con:
#         words.append(i)
# print(words)
# from collections import Counter
# counter=Counter(words)
# print(counter.most_common(40))
#
# from wordcloud import WordCloud
# import matplotlib.pyplot as plt
# wc=WordCloud(background_color='white',font_path='C:/Windows/Fonts/msyh.ttc')
# wc.generate_from_frequencies(counter)
# wc.to_file('D:/linshishuju/ciyun.png')
#
# vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
# transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
# tfidf=transformer.fit_transform(vectorizer.fit_transform(words))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
# sort= np.argsort(tfidf.toarray(),axis=1)[:,-5:]#排序并且拿出tfidf值最大的前5个
# names=vectorizer.get_feature_names()
# keywords=pd.Index(names)[sort]
# print(keywords)







# import jieba
# # list=['我叫杜一凡我爱学习代码']
# # cut_words=' '.join(jieba.lcut(str(list[0]),cut_all=False))
# # print(cut_words)
#
# import jieba
# list_txt=['我叫杜一凡我爱学习代码']
# cut_words=jieba.lcut(str(list_txt[0]),cut_all=False)
# print(cut_words)






#使用精准的划分方式
# cut_words=jieba.lcut(str(file_data["review"].values),cut_all=False)
# print(cut_words)

