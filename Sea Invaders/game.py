class Game(object):
    """Keeps track of the game logic and holds passed info about the game"""
    def __init__(self, DIMENSIONS, FPS):
        self.frames_passed = 1
        self.DIMENSIONS = DIMENSIONS
        self.FPS = FPS

    def increment_frames(self):
        """Run every frame, adds to the frame counter. Used for spawning logic in collector.py's ObjectCollector.process_all(game)"""
        self.frames_passed += 1


