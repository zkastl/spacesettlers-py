import uuid

class AbstractObject:

    def __init__(self, mass: int, radius: int, position: tuple=(0,0)):
        self.mass = mass
        self.original_mass = mass
        self.radius = radius
        self.position = position
        self.id = uuid.uuid4
        self.resources = None
        self.num_flags = 0
        self.respawn = True
        self.num_cores = 0
        self.num_mineable_asteroids = 0
        self.num_non_minable_asteroids = 0

        self.is_alive = False
        self.is_drawable = False
        self.is_movable = False

        # non-implementable
        #self.graphic = None