import torch
# input_size=4
# hidden_size=2
# batch_size=8
# seqlen=3
# hidden=torch.zeros(batch_size,hidden_size)
#
# senquence=torch.randn(seqlen,batch_size,input_size)
#
# cell=torch.nn.RNNCell(input_size=input_size,hidden_size=hidden_size)
# for input in senquence:
#     hidden=cell(input,hidden)
#     print(hidden)

a=[[1,2,3],[4,5,6]]
b=torch.LongTensor(a)
for i in b:
    print(type(i))
