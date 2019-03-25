import socket

def main():
    ip = socket.gethostbyname('frpi.ddns.net')
    port = 80

    message = "GET / HTTP/1.1\r\nHost: frpi.ddns.net\r\n\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(message.encode())

    print(sock.recv(2048).decode())


if __name__ == '__main__':
    main()