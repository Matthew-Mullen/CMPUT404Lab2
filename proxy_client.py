#!/usr/bin/env python3
import socket
import time
from multiprocessing import Pool
# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024
payload = f'GET / HTTP/1.0\r\nHost: {host}\r\n\r\n'
def connect(address):
    try:
        sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.connect(address)
        sock.sendall(payload)
        sock.shutdown(socket.SHUT_WR)
        allData=sock.recv(bufsize=BUFFER_SIZE)
        print(allData)
    except:
        pass
    finally:
        s.close()

def main():
    addr=[(HOST,PORT)]
    with Pool() as pool:
        pool.map(connect,addr*100)
if __name__ == "__main__":
    main()
