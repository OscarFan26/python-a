import socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client.connect(('118.25.57.174', 8100))
client.connect(('127.0.0.1', 8100))


while True:
    ask = input('请输入您要写的内容（0退出）：')
    if ask == '0':
        break
    client.send(ask.encode('utf8'))
    data = client.recv(1024)
    print(data.decode('utf8'))
client.close()
