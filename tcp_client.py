import socket


# tcp

def main():
    # 创建一个tcp套接字
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 链接服务器
    # tcp_socket.connet("192.100.200.123", 7890)
    server_ip = input("请输入服务器的ip:")
    server_port = int(input("请输入服务器的port:"))
    server_addr = (server_ip, server_port)
    tcp_socket.connect(server_addr)

    # 使用套接字收发数据
    send_data = input("请输入要发送的数据：")
    tcp_socket.send(send_data.encode("utf-8"))

    # 关闭套接字
    tcp_socket.close()

    print("sss")


if __name__ == "__main__":
    main()
