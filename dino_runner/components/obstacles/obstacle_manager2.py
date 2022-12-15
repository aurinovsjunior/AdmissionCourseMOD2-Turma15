import pygame

from dino_runner.components.obstacles.cactus2 import Cactus2
from dino_runner.utils.constants import LARGE_CACTUS

class ObstacleManager2:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Cactus2(LARGE_CACTUS))

        for obstacle2 in self.obstacles:
            obstacle2.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle2.rect):
                pygame.tima.delay(1000)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle2 in self.obstacles:
            obstacle2.draw(screen)