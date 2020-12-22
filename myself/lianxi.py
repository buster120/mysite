import pandas as pd
train_file = open("D:/linshishuju/LCSTS_ORIGIN/DATA/PART_I.txt", 'r',encoding='utf8')
train_file=train_file.read()
corpus = []
for i in range(100):
    corpus.append(train_file)
print(corpus)