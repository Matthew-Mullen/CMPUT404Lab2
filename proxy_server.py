#!/usr/bin/env python3
import socket
import time
from multiprocessing import Process
# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024
payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
def get_remote_ip(host):
    print("connecting to host",host)
    try:
        remote_ip = socket.gethostbyname(host)
    except:
        print('hostname was not resolved. Exiting')
        sys.exit()
    print(f'Ip address of {host} is {remote_ip}')
    return remote_ip

def handle_req(connection,proxy_end):
    send_full_data = connection.recv(BUFFER_SIZE)
    print(f"sending received data {send_full_data} to google")
    proxy_end.sendall(send_full_data)
    proxy_end.shutdown(socket.SHUT_WR)  # shutdown() is different from close()
    data = proxy_end.recv(BUFFER_SIZE)
    print(f"Sending received data {data} to client")
    conn.send(data)
    conn.close()

def main():
    host="www.google.com"
    port=80
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_strt:
        print("Attempting to start proxy server")
        proxy_strt.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        proxy_strt.bind((HOST,PORT))
        while True:
            conn,address=proxy_server.accept()
            print("connected by",address)
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as proxy_end:
                print("connecting to google")
                remote_ip = get_remote_ip(host)
                proxy_end.connect((remote_ip, port))
                process=Process(handle_req,args=(conn,proxy_end))
                process.daemon=True
                process.start()


if __name__ == "__main__":
    main()
