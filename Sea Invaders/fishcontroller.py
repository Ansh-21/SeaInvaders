from fish import Fish
from collector import ObjectCollector

class FishController(ObjectCollector):
    """Controls Fish!"""
    def __init__(self, SPAWNING_SPEED, SPEED):
        self.type = "controller"
        ObjectCollector.__init__(self)
        self.spawning_speed = SPAWNING_SPEED
        self.speed = SPEED

    def process(self, game):
        if game.frames_passed % (game.FPS/self.spawning_speed) == 1:
            fish = Fish(game.DIMENSIONS, self.speed)

