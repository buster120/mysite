import torch
import time
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import Dataset,DataLoader
import gzip
import csv
import torch.nn.utils.rnn as F
import torch.optim as optim
import math
import keras
from sklearn.feature_extraction.text import CountVectorizer, HashingVectorizer, TfidfTransformer,TfidfVectorizer
import numpy as np
import pandas as pd
from gensim.models import Word2Vec
import time
import torch
import ast
from sklearn.model_selection import train_test_split
from keras.preprocessing.text import Tokenizer
hidden_size=50
batch_size=64
n_layer=2
n_epochs=100
n_chars=10599
use_gpu=False
class TrainDataset(Dataset):
    def __init__(self):
        file_data = pd.read_csv("D:/linshishuju/shuju.csv", encoding='utf8')
        sentences = []
        for i in range(len(file_data)):
            sentences.append(ast.literal_eval(file_data.list_process[i]))
        train_x, _, train_y, _ = train_test_split(sentences, file_data.label.values, test_size=0.1,
                                                            random_state=1)
        all_data = sentences
        from keras.preprocessing.text import Tokenizer
        from keras.preprocessing.sequence import pad_sequences
        tokenizer = Tokenizer()  # 分词器
        tokenizer.fit_on_texts(all_data)  # 生成一个词典
        sequences = tokenizer.texts_to_sequences(all_data)  # 将文档转换为向量
        word_index = tokenizer.word_index
        train_x_seq = tokenizer.texts_to_sequences(train_x)
        #train_x_seq=torch.LongTensor(train_x_seq)
        self.train_x_seq=train_x_seq
        self.len=len(train_x)
        self.train_y=torch.from_numpy(train_y).view(-1,1)
        seq_lengths = []
        for arr in self.train_x_seq:
            a = len(arr)
            seq_lengths.append(a)
        seq_lengths = torch.LongTensor(seq_lengths)
        # make tensor of name, BatchSize x SeqLen
        seq_tensor = torch.zeros(len(train_x_seq), seq_lengths.max().item()).long()
        # 先创建一个都是0，但是符合姓名序列维度的二阶张量
        for idx, (seq, seq_len) in enumerate(zip(train_x_seq, seq_lengths), 0):
            seq_tensor[idx, :seq_len] = torch.Tensor(seq)
        # 将每个单词对应的ASCII码值放入seq_tensor
        # sort by length to use pack_padded_sequence
        seq_lengths, perm_idx = seq_lengths.sort(dim=0, descending=True)  # 做降序排序
        self.seq_tensor = seq_tensor[perm_idx]
        self.train_y = train_y[perm_idx]
        self.seq_lengths=seq_lengths
        print(self.seq_tensor)
    def __getitem__(self,index):  #返回名字，以及对应国家在字典里的序号
        return self.seq_tensor[index],self.train_y[index],self.seq_lengths[index]
    def __len__(self):
        return self.len
    def getseq_lengths(self):
        return self.seq_lengths


class TestDataset(Dataset):
    def __init__(self):
        file_data = pd.read_csv("D:/linshishuju/shuju.csv", encoding='utf8')
        sentences = []
        for i in range(len(file_data)):
            sentences.append(ast.literal_eval(file_data.list_process[i]))
        _, test_x, _, test_y = train_test_split(sentences, file_data.label.values, test_size=0.1,
                                                            random_state=1)
        all_data = sentences
        from keras.preprocessing.text import Tokenizer
        tokenizer = Tokenizer()  # 分词器
        tokenizer.fit_on_texts(all_data)  # 生成一个词典
        sequences = tokenizer.texts_to_sequences(all_data)  # 将文档转换为向量
        word_index = tokenizer.word_index
        test_x_seq = tokenizer.texts_to_sequences(test_x)
        self.test_x_seq=test_x_seq
        self.len=len(test_x)
        self.test_y=torch.from_numpy(test_y).view(-1,1)
        seq_lengths = []
        for arr in self.test_x_seq:
            a = len(arr)
            seq_lengths.append(a)
        seq_lengths = torch.LongTensor(seq_lengths)
        # make tensor of name, BatchSize x SeqLen
        seq_tensor = torch.zeros(len(test_x_seq), seq_lengths.max().item()).long()
        # 先创建一个都是0，但是符合姓名序列维度的二阶张量
        for idx, (seq, seq_len) in enumerate(zip(test_x_seq, seq_lengths), 0):
            seq_tensor[idx, :seq_len] = torch.Tensor(seq)
        # 将每个单词对应的ASCII码值放入seq_tensor
        # sort by length to use pack_padded_sequence
        seq_lengths, perm_idx = seq_lengths.sort(dim=0, descending=True)  # 做降序排序
        self.seq_tensor = seq_tensor[perm_idx]
        self.test_y = test_y[perm_idx]
        self.seq_lengths = seq_lengths

    def __getitem__(self, index):  # 返回名字，以及对应国家在字典里的序号
        return self.seq_tensor[index], self.test_y[index],self.seq_lengths[index]

    def __len__(self):
        return self.len
    def getseq_lengths(self):
        return self.seq_lengths

trainset=TrainDataset()
trainloader=DataLoader(trainset,batch_size=batch_size,shuffle=False)
testset=TestDataset()
testloader=DataLoader(testset,batch_size=batch_size,shuffle=False)
# seq_train=trainset.getseq_lengths()
# seq_test=testset.getseq_lengths()
class RNNClassifier(torch.nn.Module):
    def __init__(self,input_size,hidden_size,output_size,n_layers=1,bidirectional=True):
        super(RNNClassifier,self).__init__()
        self.hidden_size=hidden_size
        self.n_layers=n_layers
        self.n_directions=2 if bidirectional else 1
        self.embedding=torch.nn.Embedding(input_size,hidden_size) #将每个字母的维度由10599(input_size)变为20(hidden_size)
        self.gru=torch.nn.GRU(hidden_size,hidden_size,n_layers,bidirectional=bidirectional)
        self.fc=torch.nn.Linear(hidden_size*self.n_directions,output_size)
        self.sigmoid=torch.nn.Sigmoid()
    def _init_hidden(self,batch_size):
        hidden=torch.zeros(self.n_layers*self.n_directions,batch_size,self.hidden_size)
        return create_tensor(hidden)
    def forward(self,input,seq_lengths):
        # input shape : B x S -> S x B ,这是embedding需要的维度
        input=input.t()
        batch_size=input.size(1)
        hidden=self._init_hidden(batch_size)
        embedding=self.embedding(input)
        #得到的嵌入的维度是(seqlen,batchsize,hiddensize)
        gru_input=F.pack_padded_sequence(embedding,seq_lengths)#seq_lengths是一个序列，里边的每个值是每个名字的长度
        #该功能就是为了提高运行效率，将每句话中补的0不参与运算，具体实现方法看pytorch文档！！这里不要多做纠结
        #gru_input的维度和embedding是一样的，放心！
        output,hidden=self.gru(gru_input,hidden)
        if self.n_directions==2:
            hidden_cat=torch.cat([hidden[-1],hidden[-2]],dim=1)
        else:
            hidden_cat=hidden[-1]
        fc_output=self.sigmoid(self.fc(hidden_cat))
        return fc_output


def create_tensor(tensor):
    if use_gpu:
        device=torch.device('cuda:0')
        tensor=tensor.to(device)
    return tensor



def trainModel():
    total_loss = 0
    for i, data in enumerate(trainloader, 1):
        inputs, target,seq_train=data
        target=target.float()
        target = torch.Tensor(target).view(-1, 1)

        output = classifier(inputs, seq_train)
        loss = criterion(output, target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss += loss.item()
        if i % 10 == 0:
            print(f'[{time_since(start)}]Epoch{epoch}', end='')
            print(f'[{i * len(inputs)}/{len(trainset)}]', end='')
            print(f'loss={total_loss / (i * len(inputs))}')
    return total_loss

def testModel():
    correct = 0
    total = len(testset)
    print('evaluating trained model ...')
    with torch.no_grad():
        for i, (inputs,target,seq_test) in enumerate(testloader, 1):
            target = target.float()
            target = torch.Tensor(target).view(-1, 1)
            output = classifier(inputs, seq_test)
            pred = output.max(dim=1, keepdim=True)[1]
            correct += pred.eq(target.view_as(pred)).sum().item()
        percent = '%.2f' % (100 * correct / total)
        print(f'Test set:Accuracy{correct}/{total} {percent}%')
    return correct / total
def time_since(since):
    s=time.time()-since
    m=math.floor(s/60)
    s-=m*60 #这里边m是一个整数。
    return '%dm %ds'%(m,s)#最后的结果是m分零s秒

#第一步
if __name__=='__main__':
    classifier=RNNClassifier(n_chars,hidden_size,1,n_layer)
    #n_chars每一个字母的one-hot向量，hidden_size是输出的隐层的维度，n_country是一共有多少个分类，n_layer是用于设置你的gru是几层
    if use_gpu:
        device=torch.device('cuda:0')
        classifier.to(device)
    criterion=torch.nn.BCELoss(size_average=True)
    optimizer=torch.optim.Adam(classifier.parameters(),lr=0.001)
    start=time.time()
    print('Training for %d epochs...'%n_epochs)
    acc_list=[]
    for epoch in range(1,n_epochs+1):
        trainModel()
        acc=testModel()
        acc_list.append(acc)