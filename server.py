import socket
import os

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", 4059))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(5)

print(f"Server running on {HOST}:{PORT}")

while True:
    conn, addr = server.accept()
    print("Connected:", addr)

    data = conn.recv(1024)

    if data:
        print("Message:", data.decode(errors="ignore"))
        conn.send(b"OK")

    conn.close()