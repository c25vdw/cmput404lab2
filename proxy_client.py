import socket
import argparse
from multiprocessing import Pool, Process

payload = f'GET / HTTP/1.1\r\nHost: www.google.com\r\n\r\n'

parser = argparse.ArgumentParser(description="proxy client")
parser.add_argument('--hostname', '-H', default='www.google.com', type=str)
parser.add_argument('--port', '-p', default=80, type=int)
buffer_size = 1024


def main():
    args = parser.parse_args()

    with Pool(processes=4) as pool:
        pool.map(launch_request, [args for i in range(3)])


def launch_request(args):
    print(f"connecting to {args.hostname}:{args.port}")
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((args.hostname, args.port))
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
