#!/usr/bin/env python3
"""
   Copyright 2021 Lucas Zeng

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import socket
import time
from multiprocessing import Process
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
