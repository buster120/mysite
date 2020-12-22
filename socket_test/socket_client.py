#socket 客户端
import socket
client=socket.socket()   #根据指定的地址来分配一个套接口的描述字及其所用的资源
client.connect(('10.3.133.112',8000))

#client.sendall('bobby'.encode('utf8'))
# server_data=client.recv(1024)
# a=server_data.decode('utf8')
# print(f'server response:{a}')
while True:
    input_data=input()
    client.send(input_data.encode("utf8"))
    server_data=client.recv(1024)
    print('server response:{}'.format(server_data.decode('utf8')))
#client.close()