import socket
import datetime


def send_request():
    ip = socket.gethostbyname('frpi.ddns.net')
    port = 80

    message = "GET / HTTP/1.1\r\nHost: frpi.ddns.net\r\n\r\n"

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    sock.send(message.encode())
    sock.recv(2048).decode()  # blocks until response is received
    return


def number_seconds(dt1, dt2):
    diff = dt2 - dt1
    return diff.total_seconds()


def test_connection():
    t1 = datetime.datetime.now()
    send_request()  # blocks until response is received
    t2 = datetime.datetime.now()

    return number_seconds(t1, t2)


def main():
    secs = test_connection()
    print(secs)


if __name__ == '__main__':
    main()