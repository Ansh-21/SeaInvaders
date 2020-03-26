class ObjectCollector(object):
    """A holder for all game objects."""
    fish = []
    active_fish = []
    bullets = []
    controllers = []
    other = []
    def __init__(self):
        """All inheriting objects must call this method to be added to game tracking."""
        if self.objtype == "fish":
            self.__class__.fish.append(self)
        elif self.objtype == "bullet":
            self.__class__.bullets.append(self)
        elif self.objtype == "controller":
            self.__class__.controllers.append(self)
        else:
            self.__class__.other.append(self)

    @classmethod
    def process_all(cls, game, screen):
        """Process all current game objects"""
        for fish in cls.fish:
            for bullet in cls.bullets:
                fish.bullet_process(bullet)

        for fish in cls.fish:
            fish.process(game, screen)

        for bullet in cls.bullets:
            bullet.process(screen)

        for controller in cls.controllers:
            controller.process(game)

        for obj in cls.other:
            obj.process(screen, game)

        return game, screen
