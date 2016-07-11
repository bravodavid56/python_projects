import pygame


class Sun:
    """This is a movable object; represents the sun.
    Attributes:
        None.
    """
    def __init__(self, x, y, size, color):
        """Constructor for the Sun object.

        Arguments:
            x (int): x value for the center position.
            y (int): y value for the center position.
            size (int): radius for the sun.
            color (pygame.Color): the color for the sun.
        """
        self.x = x
        self.y = y
        self.size = size
        self.color = color

    def draw(self, screen):
        """draw function, draws a circle representing the sun.

        Arguments:
            screen (pygame.display): Used as a canvas for the
                draw function.
        Returns:
            None.
        """
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def change_x(self, inc):
        """change_x function, changes the x position.

        Arguments:
            inc (Int): changes the x position by the offset inc.

        Returns:
            None.
        """
        self.x += inc

    def change_y(self, inc):
        """change_y function, changes the y position.

        Arguments:
            inc (Int): changes the y position by the offset inc.

        Returns:
            None.
        """
        self.y += inc
