import socket
import time


def make_connections(active_conn, num_conn):
    """
    Generates list of new socket connections to append to active connections
    :param active_conn: number of active connections
    :param num_conn: number of desired connections
    :return: list of new socket connections
    """
    ip = socket.gethostbyname('frpi.ddns.net')
    port = 80
    conn_list = []

    for i in range(0, active_conn-num_conn):
        conn_list += [socket_init(ip, port)]

    return conn_list


def socket_init(ip, port):
    """
    Initializes socket to IP and port given
    :param ip: IP address to connect to
    :param port: Port to connect to
    :return: socket if connection made, 0 otherwise
    """
    try:
        message = "GET / HTTP/1.1\r\nHost: frpi.hopto.org\r\n\r\n"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((ip, port))
        sock.send(message.encode())
        return sock
    except:
        return 0


def main():
    num_connections = 10
    connection_list = []

    connection_list += make_connections(len(connection_list), num_connections)



if __name__ == '__main__':
    main()