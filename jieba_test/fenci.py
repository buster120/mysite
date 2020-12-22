import pandas as pd
import numpy as np
import jieba
import re
import ast
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer,TfidfVectorizer

file_data=pd.read_csv("D:/linshishuju/shuju.csv",encoding='utf8')
file_data=file_data.tail(1000)
file_data.index=range(len(file_data))
print(file_data)