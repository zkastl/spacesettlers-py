'''
movement.py: Convenience class to allow actions to move in orientation
and positional space.

@author Zak

Original Java code by: Amy McGovern
'''
import math
from vector_2d import Vector2D

class Movement:

    MAX_TRANSLATIONAL_ACCELERATION = 62.0
    MAX_ANGLULAR_ACCELERATION = math.pi

    def __init__(self):
        self.translational_acceleration = Vector2D()

    def set_translational_acceleration(self, translationalAcceleration: Vector2D) -> None:
        self.translational_acceleration = translationalAcceleration

        if (translationalAcceleration.magnitude / Movement.MAX_TRANSLATIONAL_ACCELERATION):
            pass