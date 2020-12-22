from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer,TfidfVectorizer
import numpy as np
import pandas as pd
# 语料
corpus = [
    'This is the first document.',
    'This is the second second document.',
    'And the third one.',
    'Is this the first document?',
]
# 将文本中的词语转换为词频矩阵
vectorizer = CountVectorizer()
# 计算个词语出现的次数
X = vectorizer.fit_transform(corpus)
# 获取词袋中所有文本关键词
word = vectorizer.get_feature_names()
#print(word)   #['and', 'document', 'first', 'is', 'one', 'second', 'the', 'third', 'this'] 文章中出现的所有的词
# 查看词频结果
#print(X.toarray())  #[[0 1 1 1 0 0 1 0 1][0 1 0 1 0 2 1 0 1][1 0 0 0 1 0 1 1 0][0 1 1 1 0 0 1 0 1]] 每一句话都出现了哪些词，出现了几次


#类调用
transformer = TfidfTransformer()
#print(transformer)
#将词频矩阵X统计成TF-IDF值
tfidf = transformer.fit_transform(X)
#查看数据结构 tfidf[i][j]表示i类文本中的tf-idf权重
print(tfidf.toarray())
sort= np.argsort(tfidf.toarray(),axis=1)[:,-5:]
keywords=pd.Index(word)[sort]
print(keywords)