from fish import Fish
from collector import ObjectCollector

class FishController(ObjectCollector):
    """Controls Fish!"""
    def __init__(self, SPAWNING_SPEED, SPEED, STILLFRAMES_MAX):
        self.objtype = "controller"
        ObjectCollector.__init__(self)
        self.spawning_speed = SPAWNING_SPEED
        self.SPEED = SPEED
        self.STILLFRAMES_MAX = STILLFRAMES_MAX

    def process(self, game):
        if game.frames_passed % (game.FPS/self.spawning_speed) == 1:
            Fish(game.DIMENSIONS, self.SPEED, self.STILLFRAMES_MAX)