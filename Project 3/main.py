import pygame
import sys
from sun import Sun
from pygame.locals import *
from planet import Planet
"""SolarSystem module -- Implements a solar system with movable sun
and planets.

This module creates a visualization of our solar system,
and allows the user to move the sun, along with
the planets by doing so (due to gravity).

*****Use the arrow keys to move the sun***********************
*****Use the space bar to slightly pause the rotating planets*****

    Run the program from the command line:
        $ python main.py

Attribute(s):
    None.
"""


def main():
    """main function, creates the window and simulation
    of the solar system.

    This function enables the creation of the window, the
    game loop, the planets, and the sun.

    Arguments:
        None.

    Returns:
        None.
    """
    pygame.init()

    colors = get_planet_colors()
    planets = get_planets(colors)

    FPS = 30
    fps_clock = pygame.time.Clock()

    window_size = (800, 800)
    SURFACE = pygame.display.set_mode(window_size)
    pygame.display.set_caption("Solar System (with Pluto!)")
    SURFACE.fill((0, 0, 0))

    sun = Sun(400, 400, 25, (255, 215, 0))

    sun.draw(SURFACE)

    move_left = False
    move_right = False
    move_down = False
    move_up = False
    pause = False
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    move_up = True
                if event.key == K_DOWN:
                    move_down = True
                if event.key == K_LEFT:
                    move_left = True
                if event.key == K_RIGHT:
                    move_right = True
                if event.key == K_SPACE:
                    pause = True
            if event.type == KEYUP:
                if event.key == K_UP:
                    move_up = False
                if event.key == K_DOWN:
                    move_down = False
                if event.key == K_LEFT:
                    move_left = False
                if event.key == K_RIGHT:
                    move_right = False
                if event.key == K_SPACE:
                    pause = False
        if move_up:
            sun.change_y(-5)
            move_high(planets, 5)
        if move_down:
            sun.change_y(5)
            move_low(planets, 5)
        if move_left:
            sun.change_x(-5)
            move_west(planets, 5)
        if move_right:
            sun.change_x(5)
            move_east(planets, 5)
        if pause:
            pygame.time.delay(1000)

        SURFACE.fill((0, 0, 0))

        sun.draw(SURFACE)

        xstart = 350
        ystart = 350
        width = 100
        height = 100

        for count in range(9):
            rect = pygame.Rect(xstart, ystart, width, height)
            pygame.draw.ellipse(SURFACE, (255, 255, 255), rect, 1)
            xstart -= 50
            ystart -= 50
            width += 100
            height += 100

        rot = .25
        for count in planets:
            count.rotate(rot)
            count.draw(SURFACE)
            rot -= .009

        pygame.display.update()
        fps_clock.tick(FPS)


def move_high(planets, x):
    """move_high function, takes a list of planets
    and an offset to move the elements up.

    This function changes the y value of each
    of the planets in the list, and changes
    their j value, which is the y
    position of the center of their orbit.

    Arguments:
        planets (list): A list of planets.
            This parameter is a list of planets.
            These planets are the ones in our
            solar system.
        x (Int): An offset.
            This parameter is an integer used to
            offset the planets by x in the y direction.
    Returns:
        None.
    """
    for count in planets:
        count.change_y(-x)
        count.change_j(-x)


def move_low(planets, x):
    """move_low function, takes a list of planets
    and an offset to move the elements down.

    This function changes the y position of the planets
    by the offset x.

    Argument(s):
        planets (list): A list of planets.
            This parameter is a list of planets.
            These planets are the ones in our
            solar system.
        x (Int): An offset.
            This parameter is an integer used to
            offset the planets by x in the -y direction.
    Return(s):
        None.
    """
    for count in planets:
        count.change_y(x)
        count.change_j(x)


def move_west(planets, x):
    """move_west function, takes a parameter list of planets
    and an offset x to move the planets to the left.

    This function moves the planets in the list by an offset of
    x to the left.

    Argument(s):
        planets (list): A list of planets.
            This parameter is a list of planets.
            These planets are the ones in our
            solar system.
        x (Int): An offset.
            This parameter is an integer used to
            offset the planets by x in the -x direction.
    Return(s):
        None.
    """
    for count in planets:
        count.change_x(-x)
        count.change_i(-x)


def move_east(planets, x):
    """move_east function, takes a list of planets and
    an offset x, and moves the planets east.

    This function moves the planets in the list to the
    right by an offset x.

    Argument(s):
        planets (list): A list of planets.
            This parameter is a list of planets.
            These planets are the ones in our
            solar system.
        x (Int): An offset.
            This parameter is an integer used to
            offset the planets by x in the y direction.
    Return(s):
        None.
    """
    for count in planets:
        count.change_x(x)
        count.change_i(x)


def get_planet_colors():
    """get_planet_colors function, returns a list of
    planet colors.

    This function returns a list of the planet colors
    in order from closest to the sun, to farthest.

    Argument(s):
        None.
    Return(s):
        list: Returns a list of the planetary colors.
    """
    p1c = pygame.Color(117, 74, 58)
    p2c = pygame.Color(213, 154, 28)
    p3c = pygame.Color(58, 80, 140)
    p4c = pygame.Color(131, 54, 44)
    p5c = pygame.Color(217, 205, 183)
    p6c = pygame.Color(209, 206, 189)
    p7c = pygame.Color(127, 147, 158)
    p8c = pygame.Color(93, 200, 236)
    p9c = pygame.Color(123, 85, 49)

    return [p1c, p2c, p3c, p4c, p5c, p6c, p7c, p8c, p9c]


def get_planets(colors):
    """get_planets function, takes a list of colors
    and creates a list of planets.

    This function takes in a list of colors and assigns
    these colors to planets, and creates a list
    of planets.

    Argument(s):
        colors (list): A list of colors to instantiate
            the planets.
    Return(s):
        list: Returns a list of planets to be used in
            the main visualization loop.
    """
    xstart = 350
    ystart = 350
    sx = 400
    sy = 400
    angle = 0
    size = 10
    offset = 500
    planets = [Planet(0, 0, 0, 0, 0, 0, (0, 0, 0), 0) for count in range(9)]
    index = 0
    for count in planets:
        count.x = xstart
        count.y = ystart
        count.i = sx
        count.j = sy
        count.angle = angle
        count.size = size
        count.offset = offset
        count.color = colors[index]
        xstart -= 50
        ystart -= 50
        offset += 100
        index += 1
    return planets

if __name__ == "__main__":
    main()