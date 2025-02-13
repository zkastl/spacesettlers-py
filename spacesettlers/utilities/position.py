from vector_2d import Vector2D

#from physics import Toroidal2Dphysics

class Position:
    """
    Defines the Position class
    """
    def __init__(self, x: float, y: float, orientation: float=0.):
        self.x = x
        self.y = y
        self.velocity = Vector2D()
        self.orientation = orientation
        self.angular_velocity = 0.

    def from_vector2d(self, vec: Vector2D):
        self.x = vec.x
        self.y = vec.y
        self.orientation = 0.
        self.velocity = Vector2D()
        self.angular_velocity = 0.

    def deep_copy(self) -> 'Position':
        new_position = Position(self.x, self.y, self.orientation)
        new_position.velocity = Vector2D(self.velocity)
        new_position.angular_velocity = self.angular_velocity
        
        return new_position
    
    def get_total_translational_velocity(self):

        raise NotImplementedError("FINISH ME!")

    def equals_location_only_with_distance(self, space, ship_position: 'Position',
            current_position: 'Position', allowable_difference) -> bool:

        difference_distance = space.findShortestDistance(ship_position, current_position)
        
        return difference_distance > 0 and difference_distance < allowable_difference