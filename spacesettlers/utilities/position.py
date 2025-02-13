from vector_2d import Vector2D

class Position:
    
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y
        self.velocity = Vector2D()
        self.orientation = 0.
        self.angular_velocity = 0.

    def __init__(self, x: float, y: float, orientation: float):
        self.x = x
        self.y = y
        self.velocity = Vector2D()
        self.orientation = orientation
        self.angular_velocity = 0.

    def __init__(self, vec: Vector2D):
        self.x = vec.x
        self.y = vec.y
        self.orientation = 0.
        self.velocity = Vector2D()
        self.angular_velocity = 0.

    def deepCopy(self) -> 'Position':
        new_position = Position(self.x, self.y, self.orientation)
        new_position.velocity = Vector2D(self.velocity)
        new_position.angular_velocity = self.angular_velocity
        
        return new_position
    
    def get_total_translational_velocity(self):
        return self.velocity.