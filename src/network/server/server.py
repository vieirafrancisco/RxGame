import sys
import socket

import rx
from rx import operators as ops

from src.config import SERVER_HOST, SERVER_PORT
from src.utils import Request


class Server:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    @property
    def address(self):
        return (self.host, int(self.port))

    def listen(self):
        pass


class GameServer(Server):
    def __init__(self, host=SERVER_HOST, port=SERVER_PORT):
        super().__init__(host, port)
        self.players = {}

    def __str__(self):
        return f"GameServer<host: {self.host}>"

    def dispatch(self, request):
        if request.method == "CONNECT":
            return "Connection Accepted!"
        if request.method == "SEND":
            id, x, y = request.prep_data
            self.players.update({id: (x, y)})
            print(self.players[id])
            return f"Save player: {id}"
        if request.method == "GET":
            data = ""
            for pid, (px, py) in self.players.items():
                data += f"{pid}&{px}&{py} "
            return data
        return "None"

    def listen(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(self.address)
            print(f'{self} listening on port {self.port}')
            while True:
                s.listen()
                conn, addr = s.accept()
                with conn:
                    print('Connected by', addr)
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        request = Request.decode(data)
                        response = self.dispatch(request)
                        conn.sendall(response.encode())
