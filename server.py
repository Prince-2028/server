import socket

server = socket.socket()
server.bind(("0.0.0.0", 4059))
server.listen(1)

print("Waiting...")

conn, addr = server.accept()

msg = conn.recv(1024).decode()

print("Message:", msg)

conn.close()