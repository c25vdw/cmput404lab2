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
import argparse
from multiprocessing import Pool

payload = f'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'

parser = argparse.ArgumentParser(description="proxy client")
parser.add_argument('--host', '-H', default='127.0.0.1', type=str)
parser.add_argument('--port', '-p', default=8001, type=int)
buffer_size = 1024


def main():
    args = parser.parse_args()
    print(f"assuming proxy at {args.host}:{args.port}")

    with Pool(processes=4) as pool:
        pool.map(launch_request, [args for _ in range(3)])


def launch_request(args):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.host, args.port))
    print(">>> sending payload")
    s.sendall(payload.encode())
    s.shutdown(socket.SHUT_WR)
    # continue accepting data until no more left
    full_data = b""
    while True:
        data = s.recv(buffer_size)
        if not data:
            break
        full_data += data
    print("<<< finished")


if __name__ == '__main__':
    main()
