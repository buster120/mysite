#线性回归
import torch
import torch.nn as nn
N,D_in,H,D_out=64,1000,100,10
#随机创建一些训练数据
x=torch.randn(N,D_in)
y=torch.randn(N,D_out)

model=torch.nn.Sequential(
    torch.nn.Linear(D_in,H,bias=False),
    torch.nn.ReLU(),
    torch.nn.Linear(H,D_out,bias=False),
)
torch.nn.init.normal_(model[0].weight)
torch.nn.init.normal_(model[2].weight)
learning_rate=1e-6
loss_fn=nn.MSELoss(reduction='sum')
for it in range(400):
    y_pred=model(x)
    loss=loss_fn(y_pred,y)
    print(it,loss.item())
    model.zero_grad()
    loss.backward()
    with torch.no_grad():
        for param in model.parameters():
            param-=learning_rate*param.grad
print(y-y_pred)



