# This is like a mutable tuple to allow users to create a Point or Vector with labelled x and y components.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y