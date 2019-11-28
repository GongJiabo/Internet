import socket


def send_file_2_client(new_client_socket, client_addr):
    # 1. 接收客户端需要下载的文件名
    file_name = new_client_socket.recv(1024).decode("utf-8")
    print("客户端(%s)需要下载的文件是:%s" % (str(client_addr), file_name))

    file_content = None
    # 2. 打开这个文件，读取数据
    try:
        f = open(file_name, "rb")
        file_content = f.read()
        f.close()
    except Exception as ret:
        print("没有要下载的文件:%s" % file_name)

    # 3. 发送文件给客户端
    if file_content:
        new_client_socket.send(file_content)


def main():
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server.bind(("", 7890))

    tcp_server.listen(128)

    while True:
        new_client_socket, client_addr = tcp_server.accept()

        send_file_2_client(new_client_socket, client_addr)

        new_client_socket.close()

    tcp_server.close()


if __name__ == "__main__":
    main()