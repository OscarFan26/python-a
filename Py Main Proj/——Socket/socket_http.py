import socket
from urllib.parse import urlparse


def get_url(url):
    """通过socket请求HTML"""
    url = urlparse(url)
    host = url.netloc
    path = url.path
    print(url, host, path)
    if path == '':
        path = '/'
    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))
    client.send('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n'.format(path, host).encode('utf8'))
    a = ('GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\nhello'.format(path, host).encode('utf8'))
    print('显示为：', a)
    data = b''
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break
    data = data.decode('utf8')
    html_data = data.split('\r\n\r\n')[1]
    print(data, '\n\n===============\n\n', html_data, '\n\n', type(html_data))
    client.close()


if __name__ == '__main__':
    get_url('https://www.baidu.com')
