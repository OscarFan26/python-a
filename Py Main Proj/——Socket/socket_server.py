import socket
import threading
server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
server.bind(('127.0.0.1', 8100))
server.listen()

def server_p(sock,addr):
    while True:
        data = sock.recv(1024)
        print('对方发过来的信息：', data.decode('utf8'))
        if data == '0':
            break
        ask = input('请输入您要写的内容：(0退出)')
        sock.send(ask.encode('utf8'))

    sock.close()
while True:
    sock, addr = server.accept()
    t1 = threading.Thread(target=server_p, args=(sock,addr))
    t1.start()
server.close()
