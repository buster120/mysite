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

hidden_size=100
batch_size=256
n_layer=1
n_epochs=100
n_chars=128
use_gpu=False


class NameDataset(Dataset):
    def __init__(self,is_train_set=True):
        filename='D:/linshishuju/names_train.csv.gz'if is_train_set else 'D:/linshishuju/names_test.csv.gz'
        with gzip.open(filename,'rt') as f:
            reader=csv.reader(f)
            rows=list(reader)
        self.names=[row[0] for row in rows]
        self.len=len(self.names)
        self.countries=[row[1] for row in rows]
        self.country_list=list(sorted(set(self.countries)))
        self.country_dict=self.getCountryDict()
        self.country_num=len(self.country_list)
    def __getitem__(self,index):  #返回名字，以及对应国家在字典里的序号
        return self.names[index],self.country_dict[self.countries[index]]
    def __len__(self):
        return self.len
    def getCountryDict(self): #字典里的values和列表的索引是一样的,根据国家去找序号
        country_dict=dict()
        for idx,country_name in enumerate(self.country_list,0):
            country_dict[country_name]=idx
        return country_dict
    def idx2country(self,index):  #根据列表里的索引找国家。比如你将来根据名字输入，经过分析，得到一个序列，你就可以拿这个序列从字典里把国家找出来
        return self.country_list[index]
    def getCountriesNum(self):
        return self.country_num

trainset=NameDataset(is_train_set=True)
trainloader=DataLoader(trainset,batch_size=batch_size,shuffle=True)
testset=NameDataset(is_train_set=False)
testloader=DataLoader(testset,batch_size=batch_size,shuffle=True)

n_country=trainset.getCountriesNum()

class RNNClassifier(torch.nn.Module):
    def __init__(self,input_size,hidden_size,output_size,n_layers,bidirectional=True):
        super(RNNClassifier,self).__init__()
        self.hidden_size=hidden_size
        self.n_layers=n_layers
        self.n_directions=2 if bidirectional else 1
        self.embedding=torch.nn.Embedding(input_size,hidden_size) #将每个字母的维度由128(input_size)变为100(hidden_size)
        self.gru=torch.nn.GRU(hidden_size,hidden_size,n_layers,bidirectional=bidirectional)
        self.fc=torch.nn.Linear(hidden_size*self.n_directions,output_size)
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
        print(hidden.shape)
        if self.n_directions==2:
            hidden_cat=torch.cat([hidden[-1],hidden[-2]],dim=1)
        else:
            hidden_cat=hidden[-1]
        print(len(hidden_cat),len(hidden_cat[0]))
        fc_output=self.fc(hidden_cat)

        return fc_output

def name2list(name):
    arr=[ord(c) for c in name]
    return arr,len(arr)

def create_tensor(tensor):
    if use_gpu:
        device=torch.device('cuda:0')
        tensor=tensor.to(device)
    return tensor

def make_tensors(names,countries):
    sequences_and_lengths=[name2list(name)for name in names]
    name_sequences=[sl[0] for sl in sequences_and_lengths]
    seq_lengths=torch.LongTensor([sl[1]for sl in sequences_and_lengths])
    #这就是每个名字的长度！！
    countries=countries.long()
    # make tensor of name, BatchSize x SeqLen
    seq_tensor=torch.zeros(len(name_sequences),seq_lengths.max()).long()
    #先创建一个都是0，但是符合姓名序列维度的二阶张量
    for idx,(seq,seq_len) in enumerate(zip(name_sequences,seq_lengths),0):
        seq_tensor[idx,:seq_len]=torch.LongTensor(seq)
    #将每个单词对应的ASCII码值放入seq_tensor
    # sort by length to use pack_padded_sequence
    seq_lengths,perm_idx=seq_lengths.sort(dim=0,descending=True)  #做降序排序，perm_idx是排序后元素之前的索引
    seq_tensor=seq_tensor[perm_idx]
    countries=countries[perm_idx]
    return create_tensor(seq_tensor),create_tensor(seq_lengths),create_tensor(countries)

def trainModel():
    total_loss=0
    for i,(names,countries) in enumerate(trainloader,1):
        inputs,seq_lengths,target=make_tensors(names,countries)

        output=classifier(inputs,seq_lengths)
        loss=criterion(output,target)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        total_loss+=loss.item()
        if i%10==0:
            print(f'[{time_since(start)}]Epoch{epoch}',end='')
            print(f'[{i*len(inputs)}/{len(trainset)}]', end='')
            print(f'loss={total_loss/(i*len(inputs))}')
    return total_loss

def testModel():
    correct=0
    total=len(testset)
    print('evaluating trained model ...')
    with torch.no_grad():
        for i,(names,countries) in enumerate(testloader,1):
            inputs,seq_lengths,target=make_tensors(names,countries)
            output=classifier(inputs,seq_lengths)
            pred=output.max(dim=1,keepdim=True)[1]
            correct+=pred.eq(target.view_as(pred)).sum().item()
        percent='%.2f'%(100*correct/total)
        print(f'Test set:Accuracy{correct}/{total} {percent}%')
    return correct/total
def time_since(since):
    s=time.time()-since
    m=math.floor(s/60)
    s-=m*60 #这里边m是一个整数。
    return '%dm %ds'%(m,s)#最后的结果是m分零s秒

#第一步
if __name__=='__main__':
    classifier=RNNClassifier(n_chars,hidden_size,n_country,n_layer)
    #n_chars每一个字母的one-hot向量，hidden_size是输出的隐层的维度，n_country是一共有多少个分类，n_layer是用于设置你的gru是几层
    if use_gpu:
        device=torch.device('cuda:0')
        classifier.to(device)
    criterion=torch.nn.CrossEntropyLoss()
    optimizer=torch.optim.Adam(classifier.parameters(),lr=0.001)
    start=time.time()
    print('Training for %d epochs...'%n_epochs)
    acc_list=[]
    for epoch in range(1,n_epochs+1):
        trainModel()
        acc=testModel()
        acc_list.append(acc)