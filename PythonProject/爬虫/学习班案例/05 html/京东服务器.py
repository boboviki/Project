import socket

sock = socket.socket()
sock.bind(("127.0.0.1", 8888))
sock.listen(3)

print("京东服务器已经启动...")
while 1:
    conn, addr = sock.accept()
    data = conn.recv(1024)
    print("data:", data)

    # 请求data解析  获取路径 path
    path = data.decode().split("\r\n")[0].split(" ")[1]
    print("path", path)

    conn.send(b"HTTP/1.1 200 ok\r\ncontent-type:text/html\r\n\r\nOK")

    conn.close()
