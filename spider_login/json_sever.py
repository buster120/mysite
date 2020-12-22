#服务在用户登录成功之后，给用户返回一段字符串（够复杂，生成算法别人伪造不了）
#每次用户请求的时候带上参数username（很不安全）
"""
user_info={
    "sessionid":"bobby"
}
浏览器每一次请求（所有url）都会自动带上这个sessionid（就是cookie）  服务器通过拦截这个id映射出用户名，就可以验证出这是哪一个用户的请求（查找文档存在于服务器支持的数据库或者缓存中）
1.如何告知浏览器这个sessionid
 set-cookie
2.如何确保浏览器每一次登录都带上这个sessionid
浏览器的默认行为


session和cookie的区别
    1.session是由服务器维护的，并由服务器解释，通过set—cookie交给浏览器
    2.cookie是浏览器的工具，并在后续的每一次请求中都带上这些值

"""


# socket 服务端
import socket
import threading

server = socket.socket()  # 根据指定的地址来分配一个套接口的描述字及其所用的资源
server.bind(('0.0.0.0', 8002))
server.listen()

user_info={
    "sessionid":"bobby"
}


def handle_sock(sock, addr):
    # 获取客户端连接并启动线程去处理
    while True:
        # sock.send('welcome to server!'.encode('utf8'))
        tmp_data = sock.recv(1024)
        print(tmp_data.decode('utf8'))
        response_template = '''HTTP/1.1 200 OK
Content-type: text/html
Set-Cookie: name=bobby
Set-Cookie: course_id=78
Set-Cookie: sessionid=abc123; Expires=Wed, 09 Jun 2021 10:18:14 GMT

{}


'''

        # input_data=input()
        sock.send(response_template.encode('utf8'))


while True:
    # 阻塞等待连接
    sock, addr = server.accept()
    # 启动一个线程去处理新的用户连接
    client_thread = threading.Thread(target=handle_sock, args=(sock, addr))
    client_thread.start()
