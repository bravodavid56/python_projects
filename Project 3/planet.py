import pygame
import math


class Planet:
    """The Planet class represents the planets that orbit the sun.

    Attributes:
        None.
    """
    def __init__(self, x, y, i, j, angle, size, color, offset):
        """Constructor for the Planet class.

         Takes in several parameters, to create a planet that orbits
         the sun.

         Arguments:
             x (Int): the x value for the center of the planet
             y (Int): the y value for the center of the planet
             i (Int): the x value for the center of the orbit
             j (Int): the y value for the center of the orbit
             angle (Int): Used to simulate a circular motion.
             size (Int): the radius of the planet
             color (pygame.Color): the color of the planet
             offset (Int): an offset representing how far away
                from the center of the orbit.
        """
        self.x = x
        self.y = y
        self.i = i
        self.j = j
        self.angle = angle
        self.size = size
        self.color = color
        self.offset = offset

    def draw(self, screen):
        """draw method, draws a circle representing the planet.

        Draws a circle representing the planet.

        Arguments:
            screen (pygame.display): The canvas for the drawing.

        Returns:
            None.
        """
        pygame.draw.circle(screen, self.color, [self.x, self.y], self.size)

    def change_x(self, inc):
        """change_x method, changes x by Int inc

        Changes the x position of the planet.

        Arguments:
            inc (Int): Represents an offset to change x by.
        Returns:
            None.
        """
        self.x += inc

    def change_y(self, inc):
        """change_y method, changes y by Int inc

        Changes the y position of the planet.

        Arguments:
            inc (Int): Represents an offset to change y by.
        Returns:
            None.
        """
        self.y += inc

    def change_i(self, inc):
        """change_i method, changes i by Int inc

        Changes the i position of the planet, which
        represents the x position of the orbit.

        Arguments:
            inc (Int): Represents an offset to change i by.
        Returns:
            None.
        """
        self.i += inc

    def change_j(self, inc):
        """change_j method, changes j by Int inc

        Changes the j position of the planet, which
        represents the y position of the orbit.

        Arguments:
            inc (Int): Represents an offset to change j by.
        Returns:
            None.
        """
        self.j += inc

    def rotate(self, velocity):
        """rotate method, used to simulate orbit
        by a given velocity.

        Changes the x and y positions based on a changing angle
        affected by the velocity. A higher velocity represents
        a faster rotation.

        Arguments:
            velocity (Int): Represents the rotational speed.
        Returns:
            None.
        """
        self.x = int(self.offset * velocity * math.cos(self.angle) + self.i)
        self.y = int(self.offset * velocity * math.sin(self.angle) + self.j)
        self.angle = self.angle + velocity

