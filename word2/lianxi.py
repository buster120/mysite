from gensim.models import Word2Vec
# import numpy as np
sentences=[['我','的','名字','是'],['我','的','兄弟','是']]
model = Word2Vec(sentences, size=50, window=5, min_count=0, workers=4)
# a=model.wv.vectors
# print(a)
# # print(len(a))
# # print(model)
# print(model.wv.index2word)
# embedding_dic=dict(zip(model.wv.index2word,model.wv.vectors)) #第一个是所有的词，第二个是所有的向量
# embedding_matrix=np.zeros((len(a),50)) #嵌入矩阵
# # print(type(embedding_dic))
# # print(embedding_matrix.shape)
# bb=model['是'].tolist()
# print(bb)


from nltk import word_tokenize

# train_words2vec=train_x_sen
# print(train_x_sen)
# test_x_sen=[['我','的','名字','是'],['我','的','兄弟','是']]
# test_words2vec = []
# dd = []
# for content in test_x_sen:
#     aa = []
#     for i in content:
#
#         bb = list(model[i])
#         for k in bb:
#             aa.append(k)
#
#     test_words2vec.append(aa)
#
#     # train_words2vec.append(dd)
#
#     # test_words2vec.append(dd)
# print(test_words2vec)
import torch
import torch.nn as nn
import torch.nn.functional as F
class Net(nn.Module):
 def __init__(self):
 super(Net, self).__init__()
 # 1 input image channel, 6 output channels, 5x5 square convolution
 # kernel
 self.conv1 = nn.Conv2d(1, 6, 5)
 self.conv2 = nn.Conv2d(6, 16, 5)
 # an affine operation: y = Wx + b
 self.fc1 = nn.Linear(16 * 5 * 5, 120)
 self.fc2 = nn.Linear(120, 84)
 self.fc3 = nn.Linear(84, 10)
 def forward(self, x):
 # Max pooling over a (2, 2) window
 x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
 # If the size is a square you can only specify a single number
 x = F.max_pool2d(F.relu(self.conv2(x)), 2)
 x = x.view(-1, self.num_flat_features(x))
 x = F.relu(self.fc1(x))
 x = F.relu(self.fc2(x))
 x = self.fc3(x)
 return x
 def num_flat_features(self, x):
 size = x.size()[1:] # all dimensions except the batch dimension
 num_features = 1
 for s in size:
 num_features *= s
 return num_features
net = Net()
print(net)