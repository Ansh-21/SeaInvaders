from collector import ObjectCollector

class Fish(ObjectCollector):
    """A class representing the 'ships' that fly towards the player. As this is underwater, we have fish instead!"""
    def __init__(self):
        ObjectCollector.__init__(self)


