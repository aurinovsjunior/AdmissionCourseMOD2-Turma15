import pygame

from dino_runner.components.obstacles.passaros import Passaros
from dino_runner.utils.constants import BIRD

class ObstacleManager3:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        if len(self.obstacles) == 0:
            self.obstacles.append(Passaros(BIRD))

        for obstacle3 in self.obstacles:
            obstacle3.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle3.rect):
                pygame.tima.delay(1000)
                game.playing = False
                break
    
    def draw(self, screen):
        for obstacle3 in self.obstacles:
            obstacle3.draw(screen)