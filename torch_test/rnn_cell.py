#将‘hello’转化为‘ohlol’
import torch
input_size=4
hidden_size=4
batch_size=1
idx2char=['e','h','l','o']
x_data=[1,0,2,2,3]
y_data=[3,1,2,3,2]
one_hot_lookup=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
x_one_hot=[one_hot_lookup[x] for x in x_data]
inputs=torch.Tensor(x_one_hot).view(-1,batch_size,input_size)
labels=torch.LongTensor(y_data).view(-1,batch_size)
#这里的y_data是分类的序列号（0,1,2,3..），交叉熵计算loss的时候会自动把他转化为one_hot。表示一维的分类序列号的话，你要用LongTensor  -.-
#而且labels是二维的，方便计算交叉熵
class Model(torch.nn.Module):
    def __init__(self,input_size,hidden_size,batch_size):
        super(Model, self).__init__()
        self.batch_size=batch_size
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.rnncell=torch.nn.RNNCell(input_size=self.input_size,hidden_size=self.hidden_size)
    def forward(self,input,hidden):
        hidden=self.rnncell(input,hidden)
        return hidden
    def init_hidden(self):
        return torch.zeros(self.batch_size,self.hidden_size)
net=Model(input_size,hidden_size,batch_size)
criterion=torch.nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(net.parameters(),lr=0.1)
for epoch in range(15):
    loss=0
    optimizer.zero_grad()
    hidden=net.init_hidden()
    print('Predicted string:',end='') #end=''自动换行
    for input,label in zip(inputs,labels):
        hidden=net(input,hidden) #计算出来的hidden即要用于计算loss，也要作为下一个字母的输入hidden,计算出来是二维的
        loss+=criterion(hidden,label)
        _,idx=hidden.max(dim=1)
        print(idx2char[idx.item()],end='')
    loss.backward()
    optimizer.step()
    print(',Epoch[%d/15] loss=%.4f'%(epoch+1,loss.item()))