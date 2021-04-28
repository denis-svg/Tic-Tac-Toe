import socket
import threading
from game import SinglePlayerGame as Game


class Server:
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.HEADER = 64
        self.FORMAT = "utf-8"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((self.IP, self.PORT))
        self.games = {}
        self.id_count = 0
        self.game_id = 0

    def handle_client(self, conn, addr, player):
        print(f"new connection {addr}")
        while True:
            msg = conn.recv(self.HEADER).decode(self.FORMAT)
            if msg:
                print(f"{addr} sent {msg}")
            if msg == "!DISCONNECT":
                break

        conn.close()

    def main(self):
        print(f"Starting server {self.IP}:{self.PORT}")
        self.server.listen(10)
        while True:
            player = ""
            conn, addr = self.server.accept()
            self.id_count += 1
            if self.id_count % 2 == 1:
                self.game_id = self.id_count // 2 + 1
                self.games[self.game_id] = Game()
                player = "X"
            else:
                player = "O"
                self.games[self.game_id].ready = True

            thread = threading.Thread(target=self.handle_client, args=(conn, addr, player))
            thread.start()
            print(f"Active connections {threading.activeCount() - 1}")


if __name__ == "__main__":
    s1 = Server(socket.gethostbyname(socket.gethostname()), 8000)
    s1.main()
