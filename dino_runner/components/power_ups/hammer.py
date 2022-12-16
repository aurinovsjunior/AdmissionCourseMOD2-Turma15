from dino_runner.utils.constants import HAMMER, HAMMER_TYPE
from dino_runner.components.power_ups.power_up import PowerUp

class Hammer(PowerUp):
    def __init__(self):
        self.image2 = HAMMER
        self.type2 = HAMMER_TYPE
        super().__init__(self.image2, self.type2)