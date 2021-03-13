import socket


class Network:
    def __init__(self):
        self.PORT = 8000
        self.HEADER = 64
        self.FORMAT = "utf-8"
        self.SERVER = "127.0.1.1"
        self.ADDR = (self.SERVER, self.PORT)
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect(self.ADDR)

