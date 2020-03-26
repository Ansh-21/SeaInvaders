class ObjectCollector(object):
    """A holder for all game objects."""
    fish = []
    bullets = []
    other = []
    def __init__(self):
        """All inheriting objects must call this method to be added to game tracking."""
        if self.type == "fish":
            self.__class__.fish.append(self)
        elif self.type == "bullet":
            self.__class__.bullets.append(self)
        else:
            self.__class__.other.append(self)

    @classmethod
    def process_all(cls, game):
        """Process all current game objects"""
        for fish_ in cls.fish:
            for bullet in cls.bullets:
                game = fish.process(bullet, game)
        
        for bullet in cls.bullets:
            bullet.process()

        for obj in cls.other:
            obj.process()

        return game