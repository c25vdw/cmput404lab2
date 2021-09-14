# Answers to Lab2 Questions

1. How do you specify a TCP socket in Python?

by calling `socket.socket`, we initiate a socket. by giving it a `SOCK_STREAM` option, we specify that the socket is a TCP socket.

2. What is the difference between a client socket and a server socket in Python?

Different socket options: server socket needs the port reuse option to keep listening on the same port. The client socket doesn't care about which port to use.

Different behaviour: server socket needs to bind to a port and host and start listening, while a client socket only needs to connect.
