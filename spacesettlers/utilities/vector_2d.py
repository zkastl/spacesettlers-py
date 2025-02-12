import math as np
from random import Random

class Vector2D:


    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.magnitude = float('nan')

    def __init__(self, b: 'Vector2D'):
        self.x = b.x
        self.y = b.y
        self.magnitude = float('nan')

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.magnitude = float('nan')

    def __eq__(self, value: 'Vector2D'):
        return  self.x == value.x and self.y == value.y
    
    def getUnitVector(self) -> 'Vector2D':
        return self.divide(self.magnitude)


    @staticmethod
    def fromAngle(angle: float, magnitude: float) -> 'Vector2D':
        return Vector2D(np.cos(angle) * magnitude, np.sin(angle) * magnitude)
    
    @staticmethod
    def getRandom(rand: Random, maxMagnitude: float) -> 'Vector2D':
        max = maxMagnitude * maxMagnitude
        x2 = rand.random() * max
        y2 = rand.random() * max

        x = np.sqrt(x2) if bool(rand.getrandbits(1)) else -np.sqrt(x2)
        y = np.sqrt(y2) if bool(rand.getrandbits(1)) else -np.sqrt(y2)

        return Vector2D(x, y)