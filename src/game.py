import pygame

from src.config import WIDTH, HEIGHT, BLACK, BLUE, FPS
from src.player import Player
from src.client import Client


class Game:
    def __init__(self, *args, **kwargs):
        self.running = False
        self.window_surface = None
        self.clock = pygame.time.Clock()

    def start(self):
        pygame.init()
        self.running = True
        self.window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
        self.player_group = pygame.sprite.GroupSingle()
        self.player = Player(self, WIDTH//2, HEIGHT//2)
        self.client = Client(self.player)

    def render(self):
        pygame.display.set_caption(f"RxGame (FPS: {round(self.clock.get_fps(), 2)})")
        self.player_group.draw(self.window_surface)
        for _, (px, py) in self.client.other_players.items():
            pygame.draw.rect(self.window_surface, BLUE, (px, py, 32, 32))

    def update(self):
        self.player_group.update()
        self.client.update()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.running = False

    def cleanup(self):
        pygame.quit()
    
    def execute(self):
        self.start()
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)
            self.window_surface.fill(BLACK)
            self.render()
            self.update()
            pygame.display.flip()
            self.clock.tick(FPS)
        self.cleanup()
