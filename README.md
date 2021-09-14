# Answers to Lab2 Questions

1. How do you specify a TCP socket in Python?

by calling `socket.socket`, we initiate a socket. by giving it a `SOCK_STREAM` option, we specify that the socket is a TCP socket.

2. What is the difference between a client socket and a server socket in Python?

Different socket options: server socket needs the port reuse option to keep listening on the same port. The client socket doesn't care about which port to use.

Different behaviour: server socket needs to bind to a port and host and start listening, while a client socket only needs to connect.

3. How do we instruct the OS to let us reuse the same bind port?

by calling `s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)`

4. What information do we get about incoming connections?

the address of incoming connection, and the socket

5. What is returned by recv() from the server after it is done sending the HTTP request?

`None`

6. https://github.com/c25vdw/cmput404lab2


# Usage

- `python3 proxy_client.py` to start a multi-thread/process client
- `python3 proxy_server.py` to start a forking server

proxy_client and proxy_server provides option to set the proxy host and port, using `--host <hostname> --port <port>`. Short hand is supported, too. For example, `python3 proxy_client.py -H 127.0.0.1 -p 8001` tells the client to assume proxy server running at 127.0.0.1:8001
