#将‘hello’转化为‘ohlol’
#这里相对于rnn——cell主要就是model和主函数里边有区别，rnn就相当于有seq_len个rnn_cell，rnn就是一个大的黑盒把rnn_cell括起来
import torch
input_size=4
hidden_size=4
batch_size=1
num_layers=1
seq_len=5
idx2char=['e','h','l','o']
x_data=[1,0,2,2,3]
y_data=[3,1,2,3,2]
one_hot_lookup=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
x_one_hot=[one_hot_lookup[x] for x in x_data]
inputs=torch.Tensor(x_one_hot).view(seq_len,batch_size,input_size)
labels=torch.LongTensor(y_data)
#labels的形状是(seqlen*batchsize,1)
class Model(torch.nn.Module):
    def __init__(self,input_size,hidden_size,batch_size,num_layers=1):
        super(Model, self).__init__()
        self.num_layers=num_layers
        self.batch_size=batch_size
        self.input_size=input_size
        self.hidden_size=hidden_size
        self.rnn=torch.nn.RNN(input_size=self.input_size,hidden_size=self.hidden_size,num_layers=num_layers)
    def forward(self,input):
        hidden=torch.zeros(self.num_layers,self.batch_size,self.hidden_size)
        out,_=self.rnn(input,hidden)
        return out.view(-1,self.hidden_size) #更改输出形状，使之为二维矩阵，可以参与计算交叉熵
    # def init_hidden(self):
    #     return torch.zeros(self.batch_size,self.hidden_size)
net=Model(input_size,hidden_size,batch_size,num_layers)
criterion=torch.nn.CrossEntropyLoss()
optimizer=torch.optim.Adam(net.parameters(),lr=0.1)
for epoch in range(15):
    optimizer.zero_grad()
    outputs=net(inputs)
    #其实弄清楚inputs，outputs的维度就可以了，inputs是三维的，outputs是二维的
    loss=criterion(outputs,labels)
    #这里边outputs和labels都是二维的
    loss.backward()
    optimizer.step()
    _,idx=outputs.max(dim=1)
    idx=idx.data.numpy()
    print('Predicted:',''.join([idx2char[x] for x in idx]),end='')
    print(',Epoch[%d/15] loss=%.3f'%(epoch+1,loss.item()))