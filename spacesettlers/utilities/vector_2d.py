import math as math
from random import Random

from position import Position

class Vector2D:

    ZERO_VECTOR = 'Vector2D'()
    X_UNIT_VECTOR = 'Vector2D'(1, 0)
    X_NEG_UNIT_VECTOR = 'Vector2D'(-1, 0)
    Y_UNIT_VECTOR = 'Vector2D'(1, 0)
    Y_NEG_UNIT_VECTOR = 'Vector2D'(-1, 0)

    HALF_PI = 0.5 * math.pi
    THREE_HALF_PI = 1.5 * math.pi
    TWO_PI = 2.0 * math.pi

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.magnitude = float('nan')

    def __init__(self, b: 'Vector2D'):
        self.x = b.x
        self.y = b.y
        self.magnitude = float('nan')

    def __init__(self, position: Position):
        self.x = position.x
        self.y = position.y
        self.magnitude = float('nan')

    def __init__(self):
        self.x = 0.0
        self.y = 0.0
        self.magnitude = float('nan')

    def __eq__(self, value: 'Vector2D'):
        return  self.x == value.x and self.y == value.y
    
    def getUnitVector(self) -> 'Vector2D':
        return self.divide(self.magnitude)
    
    def get_magnitude(self) -> float:
        self.magnitude = math.sqrt(self.x*self.x + self.y*self.y)
        return self.magnitude
    
    def get_total(self) -> float:
        return self.x + self.y

    @staticmethod
    def fromAngle(angle: float, magnitude: float) -> 'Vector2D':
        return Vector2D(math.cos(angle) * magnitude, math.sin(angle) * magnitude)
    
    @staticmethod
    def getRandom(rand: Random, maxMagnitude: float) -> 'Vector2D':
        max = maxMagnitude * maxMagnitude
        x2 = rand.random() * max
        y2 = rand.random() * max

        x = math.sqrt(x2) if bool(rand.getrandbits(1)) else -math.sqrt(x2)
        y = math.sqrt(y2) if bool(rand.getrandbits(1)) else -math.sqrt(y2)

        return Vector2D(x, y)