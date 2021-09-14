#!/usr/bin/env python3
import socket
import time
import asyncio

# define address & buffer size
HOST = ""
PORT = 8001
BUFFER_SIZE = 1024


async def main():
    server = await asyncio.start_server(handle, '127.0.0.1', 8001)
    addr = server.sockets[0].getsockname()
    print(f"start on addr {addr}")

    async with server:
        await server.serve_forever()


async def handle(r, w):
    proxy_r, proxy_w = await asyncio.open_connection('www.google.com', 80)
    buf = await r.read(BUFFER_SIZE)
    print(f">>> {buf}")

    proxy_w.write(buf)
    await proxy_w.drain()

    proxy_response = await proxy_r.read()

    print(f"<<< GOOGLE: {proxy_response}")

    w.write(proxy_response)
    await w.drain()

    proxy_w.close()
    w.close()
    await proxy_w.wait_closed()
    await w.wait_closed()


if __name__ == "__main__":
    asyncio.run(main())
