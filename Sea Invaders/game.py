class Game(object):
    """Keeps track of the game logic"""
    def __init__(self):
        self.frames_passed = 1

    def increment_frames(self):
        """Run every frame, adds to the frame counter. Used for spawning logic in collector.py's ObjectCollector.process_all(game)"""
        self.frames_passed += 1


