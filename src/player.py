import pygame
import uuid

from src.config import WHITE


class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, color=None):
        groups = (game.player_group,)
        super().__init__(groups)
        self.game = game
        self.id = str(uuid.uuid4())
        self.image = pygame.Surface((32, 32))
        self.image.fill(color or WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= 5
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += 5
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += 5
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= 5
