#!/usr/bin/env python3
from echo_server import BUFFER_SIZE
import socket
import time
from multiprocessing import Pool, Process
# define address & buffer size
TARGET_HOST = "www.google.com"
TARGET_PORT = 80

HOST = "127.0.0.1"
PORT = 8001
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # bind socket to address
        s.bind((HOST, PORT))
        # set to listening mode
        s.listen(2)

        while True:
            client_conn, addr = s.accept()
            with client_conn:
                p = Process(target=handle_client, args=(client_conn, addr))
                p.start()


def handle_client(conn, addr):
    # start a new socket that connects to google
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        # recieve data from the client
        full_data = conn.recv(BUFFER_SIZE)

        time.sleep(2)
        # connect to google and send
        s.connect((TARGET_HOST, TARGET_PORT))
        s.sendall(full_data)
        s.shutdown(socket.SHUT_WR)

        # receive from google
        res = b""
        while True:
            data = s.recv(BUFFER_SIZE)
            if not data:
                break
            res += data
        # send back to client
        conn.sendall(res)


if __name__ == "__main__":
    main()
