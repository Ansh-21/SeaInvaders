from bullet import Bullet
from collector import ObjectCollector

class Blaster(ObjectCollector):
    """A class representing the blaster that the player plays as."""
    def __init__(self):
        self.type = "blaster"
        ObjectCollector.__init__(self)

