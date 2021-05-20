import sys
import socket

import rx
from rx import operators as ops

from src.config import SERVER_HOST, SERVER_PORT
from src.utils import Request, Response


class Client:
    def __init__(self, player):
        self.player = player
        self.other_players = {}

    def update(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((SERVER_HOST, SERVER_PORT))
            request_connect = Request(method="CONNECT")
            request_send = Request(method="SEND", data=f"{self.player.id}&{self.player.rect.x}&{self.player.rect.y}")
            request_get = Request(method="GET")
            rx.of(request_connect, request_send, request_get).pipe(
                ops.map(lambda request: self.make_request(s, request)),
                ops.filter(lambda d: len(d) > 0 and "&" in d)
            ).subscribe(lambda x: self.prep_response(x))

    def make_request(self, conn, request):
        conn.sendall(request.encode())
        return conn.recv(1024).decode()

    def prep_response(self, data):
        print("Received {0} from server".format(data))
        for id, px, py in Response.prep_data(data):
            if id != self.player.id:
                self.other_players[id] = (px, py)
            