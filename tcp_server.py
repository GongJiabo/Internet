import socket


def main():
    # 1. socket创建一个套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. bind绑定ip和地址
    tcp_server.bind(("", 7890))

    # 3. listen使套接字变为可以变动链接
    tcp_server.listen(128)

    while True:
        print("等待一个新的客户端的到来...")
        # 4. accept等待客户端的链接
        client_socket, client_addr = tcp_server.accept()
        print("一个新的客户已经到来%s" % str(client_addr))

        while True:

            # 5. recv/send接收发送数据
            recv_data = client_socket.recv(1024)
            print("客户端发送过来的请求是:%s" % recv_data.decode("gbk"))
            # 如果recv解堵塞，那么有两种方式
            # a) 客户端发送过来数据 b) 客户端调用了close
            if recv_data:
                # 回送
                client_socket.send("hahaha,ok!!".encode("utf-8"))
            else:
                break

        # 6. 关闭套接字
        client_socket.close()
        print("已经服务完毕...")

    tcp_server.close()


if __name__ == "__main__":
    main()
