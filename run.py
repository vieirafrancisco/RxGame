import sys

from src import Game
from src.network.server import GameServer

def run_game():
    g = Game()
    g.execute()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "game":
            run_game()
        elif sys.argv[1] == "server":
            s = GameServer()
            s.listen()
