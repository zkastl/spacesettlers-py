from math import sqrt, cos, sin, pi
from random import Random

from position import Position

class Vector2D:
    
    ZERO_VECTOR = 'Vector2D'()
    X_UNIT_VECTOR = 'Vector2D'(1, 0)
    X_NEG_UNIT_VECTOR = 'Vector2D'(-1, 0)
    Y_UNIT_VECTOR = 'Vector2D'(1, 0)
    Y_NEG_UNIT_VECTOR = 'Vector2D'(-1, 0)

    HALF_PI = 0.5 * pi
    THREE_HALF_PI = 1.5 * pi
    TWO_PI = 2.0 * pi

    def __init__(self, x: float=0.0, y: float=0.0):
        self.x = x
        self.y = y
        self.magnitude = float('nan')

    def from_vector2d(self, b: 'Vector2D'):
        self.x = b.x
        self.y = b.y
        self.magnitude = float('nan')

    def from_position(self, position: Position):
        self.x = position.x
        self.y = position.y
        self.magnitude = float('nan')

    def __eq__(self, value: 'Vector2D'):
        return  self.x == value.x and self.y == value.y
    
    def getUnitVector(self) -> 'Vector2D':
        return self.divide(self.magnitude)
    
    def get_magnitude(self) -> float:
        self.magnitude = sqrt(self.x*self.x + self.y*self.y)
        return self.magnitude
    
    def get_total(self) -> float:
        return self.x + self.y

    @staticmethod
    def from_angle(angle: float, magnitude: float) -> 'Vector2D':
        return Vector2D(cos(angle) * magnitude, sin(angle) * magnitude)
    
    @staticmethod
    def get_random(rand: Random, max_magnitude: float) -> 'Vector2D':
        max_m = max_magnitude * max_magnitude
        x2 = rand.random() * max_m
        y2 = rand.random() * max_m

        x = sqrt(x2) if bool(rand.getrandbits(1)) else -sqrt(x2)
        y = sqrt(y2) if bool(rand.getrandbits(1)) else -sqrt(y2)

        return Vector2D(x, y)