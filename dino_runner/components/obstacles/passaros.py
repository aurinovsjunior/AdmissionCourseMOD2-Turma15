import random

from dino_runner.components.obstacles.obstacle3 import Obstacle3

class Passaros(Obstacle3):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.x = 300