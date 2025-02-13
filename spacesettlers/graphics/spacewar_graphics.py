from pygame.surface import Surface
from spacesettlers.utilities.position import Position

class SpacewarGraphics:
    
    '''
    SpacewarGraphics: Base class for all graphics in SpaceSettlers
    '''

    def __init__(self, height: int, width: int):
        self.halfheight = height / 2
        self.halfwidth = width / 2
        self.height = height
        self.width = width
        self.draw_location = None


    # Abstract methods to override in child classes.
    def get_actual_location(self) -> Position:
        raise NotImplementedError("Abstract Method: Please provide implementation.")
    
    def draw(self, surface: Surface) -> None:
        raise NotImplementedError("Abstract Method: Please provide implementation.")
    
    def is_drawable(self)-> bool:
        raise NotImplementedError("Abstract Method: Please provide implementation.")

    def set_draw_location(self, draw_location: Position) -> None:
        self.draw_location = draw_location.deepCopy()