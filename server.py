import socket
import threading
import sys

SERVER = socket.gethostbyname(socket.gethostname())
PORT = 8000
HEADER = 64
FORMAT = "utf-8"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((SERVER, PORT))


def handle_client(conn, addr):
    print(f"new connection {addr}")
    while True:
        msg = conn.recv(HEADER).decode(FORMAT)
        if msg:
            print(f"{addr} sent {msg}")
        if msg == "!DISCONNECT":
            break

    conn.close()


def main():
    print(f"Starting server {SERVER}:{PORT}")
    server.listen(10)
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active connections {threading.activeCount() - 1}")


main()