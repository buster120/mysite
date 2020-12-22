
import torch
N,D_in,H,D_out=64,1000,100,10
#随机创建一些训练数据
x=torch.randn(N,D_in)
y=torch.randn(N,D_out)
w1=torch.randn(D_in,H,requires_grad=True) #表示反向传播时，该tensor会自动求导
w2=torch.randn(H,D_out,requires_grad=True)

learning_rate=1e-6
for it in range(500):
    h=x.mm(w1) #N*H
    h_relu=h.clamp(min=0) #N*H 取范围，最小是0（也可以取最大值，但没必要）
    y_pred=h_relu.mm(w2) #N*D_out

    loss=(y_pred-y).pow(2).sum() #tensor转item
    print(it,loss)

    loss.backward()
    with torch.no_grad():  #表示不会自动求导
        w1-=learning_rate*w1.grad
        w2-=learning_rate*w2.grad
        w1.grad.zero_()
        w2.grad.zero_()
print(y-y_pred)
