#socket 服务端
import socket
import threading
server=socket.socket()   #根据指定的地址来分配一个套接口的描述字及其所用的资源
server.bind(('0.0.0.0',8000))
server.listen()
def handle_sock(sock,addr):
#获取客户端连接并启动线程去处理
    while True:
        # sock.send('welcome to server!'.encode('utf8'))
        tmp_data=sock.recv(1024)
        print(tmp_data.decode('utf8'))
        response_template='''HTTP/1.1 200 OK

<html_test>
    <head>
        <title>Build A Web Server</title>
    </head>
    <body>
        Hello World,this is a very simple HTML document.
    </body>
</html_test>


'''
        
        #input_data=input()
        sock.send(response_template.encode('utf8'))
while True:
#阻塞等待连接
    sock,addr=server.accept()
    #启动一个线程去处理新的用户连接
    client_thread=threading.Thread(target=handle_sock,args=(sock,addr))
    client_thread.start()
