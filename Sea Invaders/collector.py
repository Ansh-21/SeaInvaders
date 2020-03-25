class ObjectCollector(object):
    """A holder for all game objects."""
    instances = []
    def __init__(self):
        self.__class__.instances.append(self)

    @classmethod
    def process_all(cls):
        for instance in cls.instances:
            instance.process()
    

