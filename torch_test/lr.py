import torch
import torch.nn.functional as F
from torch.utils.data import Dataset,DataLoader
x_data=torch.Tensor([[1.0],[2.0],[3.0]])
y_data=torch.Tensor([[0],[0],[1]])
print(y_data)
class DiabetesDataset(Dataset):
    def __init__(self):
        self.x_data = torch.Tensor([[1.0], [2.0], [3.0],[4.0]])
        self.y_data = torch.Tensor([[0], [0], [1],[1]])
    def __getitem__(self,index):
        return self.x_data[index],self.y_data[index]
    def __len__(self):
        return 4
dataset=DiabetesDataset()
train_loader=DataLoader(dataset=dataset,batch_size=2,shuffle=True)

class LogisticRegressionModel(torch.nn.Module):
    def __init__(self):
        super(LogisticRegressionModel,self).__init__()
        self.linear=torch.nn.Linear(1,1)
    def forward(self,x):
        y_pred=F.sigmoid(self.linear(x))
        return y_pred
model=LogisticRegressionModel()

criterion=torch.nn.BCELoss(size_average=False) #处理二分类的交叉熵
optimizer=torch.optim.SGD(model.parameters(),lr=0.01)

for epoch in range(1000):
    for i, data in enumerate(train_loader):
        y_pred=model(x_data)
        print(y_pred)
        loss=criterion(y_pred,y_data)
        print(epoch,loss.item())

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

print("w=",model.linear.weight.item())
print("b=",model.linear.bias.item())

x_test=torch.Tensor([[-1.0]])
y_test=model(x_test)
print('y_pred=',y_test.data)
