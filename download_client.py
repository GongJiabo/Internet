import socket

def main():
    # 1. create socket
    tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2. get ip/port
    dest_ip = input("请输入下载服务器的ip:")
    dest_port = int(input("请输入下载服务器的port:"))

    # 3. link server
    tcp_socket.connect((dest_ip, dest_port))

    # 4. get filename
    download_filename = input("请输入要下载文件的名字:")

    # 5. send filename to the server
    tcp_socket.send(download_filename.encode("utf-8"))

    # 6. receive data
    recv_data = tcp_socket.recv(1024*1024)

    if recv_data:
        # 7. save data to the file
        with open("[新]" + download_filename, "wb") as f:
            f.write(recv_data)

    # 8. close the socket
    tcp_socket.close()


if __name__ == "__main__":
    main()