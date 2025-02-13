'''
movement.py: Convenience class to allow actions to move in orientation
and positional space.

@author Zak

Original Java code by: Amy McGovern
'''
import math
from vector_2d import Vector2D

class Movement:

    # Set constants for game movement.
    MAX_TRANSLATIONAL_ACCELERATION = 62.0
    MAX_ANGLULAR_ACCELERATION = math.pi

    def __init__(self):
        self.translational_acceleration = Vector2D()
        self.angular_acceleration = 0.0

    def set_translational_acceleration(self, translational_acceleration: Vector2D) -> None:
        self.translational_acceleration = translational_acceleration

        if translational_acceleration.magnitude / Movement.MAX_TRANSLATIONAL_ACCELERATION:
            ratio = translational_acceleration.get_magnitude() / Movement.MAX_TRANSLATIONAL_ACCELERATION
            self.translational_acceleration = self.translational_acceleration.multiply(1. / ratio)

    def set_angular_accleration(self, angular_accleration) -> None:
        if angular_accleration > Movement.MAX_ANGLULAR_ACCELERATION:
            self.angular_acceleration = Movement.MAX_ANGLULAR_ACCELERATION
        elif angular_accleration < -Movement.MAX_ANGLULAR_ACCELERATION:
            self.angular_acceleration = -Movement.MAX_ANGLULAR_ACCELERATION
        else:
            self.angular_acceleration = angular_accleration