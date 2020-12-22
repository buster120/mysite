import torch
from torch import nn
from torchvision import transforms
from torchvision import datasets
from torch.utils.data import DataLoader
import torch.nn.functional as F
import torch.optim as optim
batch_size=64
transform=transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.1307,),(0.3081,))
])
train_dataset=datasets.MNIST(root='D:/linshishuju/mnist/',
                             train=True,
                             download=False,
                             transform=transform)
train_loader=DataLoader(train_dataset,shuffle=True,batch_size=batch_size)
test_dataset=datasets.MNIST(root='D:/linshishuju/mnist/',
                             train=False,
                             download=False,
                             transform=transform)
test_loader=DataLoader(train_dataset,shuffle=True,batch_size=batch_size)

class InceptionA(nn.Module):
    def __init__(self, in_channels):
        super(InceptionA, self).__init__()
        self.branch1x1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch5x5_1 = nn.Conv2d(in_channels,16, kernel_size=1)
        self.branch5x5_2 = nn.Conv2d(16, 24, kernel_size=5, padding=2)
        self.branch3x3_1 = nn.Conv2d(in_channels, 16, kernel_size=1)
        self.branch3x3_2 = nn.Conv2d(16, 24, kernel_size=3, padding=1)
        self.branch3x3_3 = nn.Conv2d(24, 24, kernel_size=3, padding=1)
        self.branch_pool = nn.Conv2d(in_channels, 24, kernel_size=1)
    def forward(self, x):
        branch1x1 = self.branch1x1(x)
        branch5x5 = self.branch5x5_1(x)
        branch5x5 = self.branch5x5_2(branch5x5)
        branch3x3 = self.branch3x3_1(x)
        branch3x3 = self.branch3x3_2(branch3x3)
        branch3x3 = self.branch3x3_3(branch3x3)
        branch_pool = F.avg_pool2d(x, kernel_size=3, stride=1, padding=1)
        branch_pool = self.branch_pool(branch_pool)
        outputs = [branch1x1, branch5x5, branch3x3, branch_pool]
        return torch.cat(outputs, dim=1)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(1, 10, kernel_size=5)
        self.conv2 = nn.Conv2d(88, 20, kernel_size=5)
        self.incep1 = InceptionA(in_channels=10)
        self.incep2 = InceptionA(in_channels=20)
        self.mp = nn.MaxPool2d(2)
        self.fc = nn.Linear(1408, 10)
    def forward(self, x):
        in_size = x.size(0)
        x = F.relu(self.mp(self.conv1(x)))
        x = self.incep1(x)
        x = F.relu(self.mp(self.conv2(x)))
        x = self.incep2(x)
        x = x.view(in_size, -1)
        x = self.fc(x)
        return x

model = Net()
criterion=torch.nn.CrossEntropyLoss()
optimizer=optim.SGD(model.parameters(),lr=0.01,momentum=0.5)
def train(epoch):
    running_loss=0.0
    for batch_idx,data in enumerate(train_loader):
        inputs,target=data

        optimizer.zero_grad()
        outputs=model(inputs)
        loss=criterion(outputs,target)
        loss.backward()
        optimizer.step()

        running_loss+=loss.item()
        if batch_idx % 300 == 299:
            print('[%d,%5d] loss:%.3f'%(epoch+1,batch_idx+1,running_loss/300))
            running_loss=0.0
def test():
    correct=0
    total=0
    with torch.no_grad():
        for data in test_loader:
            inputs,target=data
            outputs=model(inputs)
            _,predicted=torch.max(outputs.data,dim=1) #_是值，predicted是位置
            total+=target.size(0)


            # print(type((predicted==labels).sum())) #<class 'torch.Tensor'>
            # print(predicted == labels) #64个true或者false组成的一维张量
            # print((predicted == labels).sum()) #是一个tensor型的数，如tensor(59)
            # print((predicted == labels).sum().item()) #是一个数，如59
            correct+=(predicted==target).sum().item()
    print('Accuracy on test set:%d %%'%(100*correct/total))
if __name__=='__main__':
    for epoch in range(10):
        train(epoch)
        test()