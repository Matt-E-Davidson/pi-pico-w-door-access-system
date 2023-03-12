import app.api_handler as api
import socket
import time


SSID, PASSWORD = '', ''


def connect_to_wifi(wlan):
    wlan.active(False)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    connection_attempts = 10
    while connection_attempts > 0:
        if wlan.status() < 0 or wlan.status() >= 3:
            break
        connection_attempts -= 1
        print('waiting for connection...')
        time.sleep(1)
    if wlan.status() != 3:
        return False
    else:
        return True


def bind_socket():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    try:
        s.bind(addr)
    except OSError:
        pass
    s.listen(1)
    return s


def accept_requests(s):

    try:
        cl, cl_addr = s.accept()
        print('client connected from', cl_addr)
        request = cl.recv(1024)
        request = str(request)
        api.process_request(request)
        time.sleep(1)
        cl.send('HTTP/1.0 200 OK\r\nContent-type: text/html\r\n\r\n')
        cl.close()
    except OSError:
        s = bind_socket()
        accept_requests(s)
