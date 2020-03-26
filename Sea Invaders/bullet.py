from collector import ObjectCollector

class Bullet(ObjectCollector):
    """A class representing the bullets shot by the blaster"""
    def __init__(self):
        self.type = "bullet"
        ObjectCollector.__init__(self)

