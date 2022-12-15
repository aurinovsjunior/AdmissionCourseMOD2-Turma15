import random

from dino_runner.components.obstacles.obstacle2 import Obstacle2

class Cactus2(Obstacle2):
    def __init__(self, image):
        self.type = random.randint(0, 2)
        super().__init__(image, self.type)
        self.rect.y = 310