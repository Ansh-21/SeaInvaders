from debugging import *

class ObjectCollector(object):
    """A holder for all game objects."""
    fish = []
    bullets = []
    controllers = []
    other = []
    blaster = None
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
            if self.objtype == "blaster":
                self.__class__.blaster = self

    @classmethod
    def process_all(cls, game, screen, debug=False):
        """Process all current game objects"""
        for fish in cls.fish:
            for bullet in cls.bullets:
                fish.bullet_process(bullet, game)

        for fish in cls.fish:
            fish.process(screen, game)

        for bullet in cls.bullets:
            bullet.process(screen)

        for controller in cls.controllers:
            controller.process(game)

        for obj in cls.other:
            obj.process(screen, game)

        if debug:
            print(len(cls.bullets))
            if len(cls.bullets) > 0:
                print(cls.bullets[0].y)

        return game, screen

    @classmethod
    def remove_this(cls, collection, obj_to_remove):
        collection = eval("cls." + str(collection))
        if obj_to_remove in collection:
            collection.remove(obj_to_remove)

    @classmethod
    def clear_all(cls):
        for fish in cls.fish:
            fish.dead = True
        for bullet in cls.bullets:
            bullet.dead = True
        cls.fish = []
        cls.bullets = []

