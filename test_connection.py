import socket
import datetime
import time
import matplotlib.pyplot as plt


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
    delay_secs = 2
    num_tests = 20  # number of times to test connection
    times = []
    delays = []

    for i in range(0, num_tests):
        times += [datetime.datetime.now()]
        delay = test_connection()
        print(delay)
        delays += [delay]

        time.sleep(delay_secs)

    plt.plot(times, delays)
    plt.xlim([times[0], times[num_tests-1]])
    plt.ylim([0, 15])
    plt.xlabel('Time of test')
    plt.ylabel('Seconds to respond')
    plt.title("Regular Server Response Time")
    plt.show()


if __name__ == '__main__':
    main()
