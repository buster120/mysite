import socket
import json
import threading
from collections import defaultdict

online_users=defaultdict(dict)  #维护用户连接
user_msgs=defaultdict(list)   #维护用户历史消息
server=socket.socket()
server.bind(('0.0.0.0',8000))
server.listen()

def handle_sock(sock,addr):
    while True:
        data=sock.recv(1024)
        json_data=json.loads(data.decode('utf8'))
        action=json_data.get('action','')
        if action=='login':
            online_users[json_data['user']]=sock  #online_users是字典名,json_data['user']是关键字,sock是值
            sock.send('登录成功'.encode('utf8'))
        elif action=='list_user':
            #获取当前在线用户
            all_users=[user for user,sock in online_users.items()]  #看不明白
            sock.send(json.dumps(all_users).encode('utf8'))
        elif action=='history_msg':
            # if json_data['user'] in action:
            #     sock.send(json.dumps(user_msgs[json_data['user']]).encode('utf8'))
            sock.send(json.dumps(user_msgs.get(json_data['user'],[])).encode('utf8'))
        elif action=='send_msg':
            if json_data['to'] in online_users:
                online_users.get(json_data['to'],None).send(json.dumps(json_data).encode('utf8'))
            user_msgs[json_data['to']].append(json_data)
        elif action=='exit':
            del online_users[json_data['user']]
            sock.send('退出成功！'.encode('utf8'))


while True:
    sock,addr=server.accept()
    client_thread=threading.Thread(target=handle_sock,args=(sock,addr))
    client_thread.start()

#1.我们用多线程去处理每个用户连接，防止主线程阻塞住
#2.自定义了消息协议并且自己完成了消息协议的解析


