import pygame
from pygame.locals import *
import sys
from map import Map1
from lord import Lord
from ally_cleric import Cleric
import constants
"""main_game Module -- Initializes the game

This module initializes the entire game, and contains the main
game loop.

Example(s):
    Run the program from the command line:
        $ python main_game.py

Attribute(s):
    None.
"""


def main():
    """main function, contains the game loop

    This function contains and manages the game loop, and
    handles any events defined in the loop. Initializes pygame,
    handles any game mechanics (turns, moves).

    Arguments:
        None.
    Returns:
        None.
    """
    pygame.init()
    FPS_CLOCK = pygame.time.Clock()
    screen = pygame.display.set_mode((constants.SCREEN_HEIGHT,
                                      constants.SCREEN_WIDTH))
    # Maps
    t = Map1()

    # to be implemented


    # Ally Units
    lord_stand = "wyvern_knight_standing.png"
    lord_walk = "wyvern_knight_moving.png"
    cleric_stand = "cleric_standing.png"
    cleric_walk = "cleric_walking.png"

    p = Lord(lord_stand, lord_walk, x=300,y=300)
    p2 = Cleric(cleric_stand, cleric_walk, x=330, y=330)

    # Groups for Ally, Enemy
    player = pygame.sprite.Group()
    player.add(p)
    player.add(p2)

    cycletime = 0
    interval = 0.5
    picnr = 0
    move = 6
    turn = True

    while True:
        # frame changes
        milli = FPS_CLOCK.tick(30)
        seconds = milli / 1000.0
        cycletime += seconds

        if cycletime > interval:
            player.update(turn, picnr)
            picnr += 1
            if picnr == len(p.stand_f) \
                    or picnr == len(p.walking_l_f)\
                    or picnr == len(p.walking_u_f)\
                    or picnr == len(p.walking_d_f)\
                    or picnr == len(p.selected_f):
                picnr = 0
            cycletime = 0

        # event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                buttons = pygame.mouse.get_pressed()
                if buttons[0]:
                    a = pygame.mouse.get_pos()
                    x = a[0]
                    y = a[1]
                    if p.rect.x < x < p.rect.x + 30 and \
                            p.rect.y + 30 > y > p.rect.y and \
                            turn:
                        if not p.done:
                            p.face = "n"
                            p.selected = True
                            p2.selected = False
                            p2.face = "s"
                        else:
                            pass
                    if p2.rect.x < x < p2.rect.x + 30 and \
                        p2.rect.y + 30 > y > p2.rect.y and \
                            turn:
                        if not p2.done:
                            p2.face = "n"
                            p.selected = False
                            p2.selected = True
                        elif turn:
                            p2.face = "s"
                            p.face = "n"
                            p.selected = True
                            p2.selected = False

            if event.type == KEYDOWN and p.face == "n" and \
                            p.c_move < move and turn:
                if event.key == K_d:
                    if p.selected:
                        p.face = "r"

                if event.key == K_a:
                    if p.selected:
                        p.face = "l"
                if event.key == K_w:
                    if p.selected:
                        p.face = "u"
                if event.key == K_s:
                    if p.selected:
                        p.face = "d"
            elif event.type == KEYDOWN and p2.face == "n" and \
                            p2.c_move < move and turn:
                if event.key == K_d:
                    if p2.selected:
                        p2.face = "r"
                if event.key == K_a:
                    if p2.selected:
                        p2.face = "l"
                if event.key == K_w:
                    if p2.selected:
                        p2.face = "u"
                if event.key == K_s:
                    if p2.selected:
                        p2.face = "d"

            if p.c_move >= move:
                p.selected = False
                if p2.c_move >= move:
                    p2.selected = False
                    turn = False

            if event.type == KEYUP and p.c_move >= move \
                    and not turn and p2.c_move >= move:
                p.face = "s"
                p2.face = "s"
            elif event.type == KEYUP and turn:
                if p.selected:
                    p.face = "n"
                    p2.face = "s"
                elif p2.selected:
                    p.face = "s"
                    p2.face = "n"
                else:
                    p.face = "s"
                    p2.face = "s"

            if event.type == KEYDOWN:
                if event.key == K_x:
                    turn = not turn
                    p.c_move = 0
                    p2.c_move = 0
                    p.selected = not p.selected
                    p.done = not p.done
                    p2.done = not p2.done

                if event.key == K_z:
                    if p.hp > 0:
                        p.hp -= 2
                        p.mhp += 2
                    if p2.hp > 0:
                        p2.hp -= 5
                        p2.mhp += 5
                if p.hp <= 0:
                    p.done = True
                if p2.hp <= 0:
                    p2.done = True
            if p.done and p2.done:
                turn = False

        snap_grid(p, p2)

        t.draw(screen)

        player.draw(screen)

        display_moves(turn, p, p2, move, screen)
        display_turn(screen, turn)
        pygame.display.update()


def snap_grid(p, p2):
    """snap_grid snaps movements to a grid of tiles

    This function takes snaps the movements of the players
    and snaps them onto a "grid" using modulo, and gives the
    illusion of players moving on tiles.

    Arguments:
        p (Lord): the main character
        p2 (Cleric): the supporting character
    Returns:
        None.
    """
    while p.rect.x % 30 != 0:
        if p.face == "l":
            p.rect.x -= 1
        if p.face == "r":
            p.rect.x += 1

    while p.rect.y % 30 != 0:
        if p.face == "u":
            p.rect.y -= 1
        if p.face == "d":
            p.rect.y += 1

    while p2.rect.x % 30 != 0:
        if p2.face == "l":
            p2.rect.x -= 1
        if p2.face == "r":
            p2.rect.x += 1

    while p2.rect.y % 30 != 0:
        if p2.face == "u":
            p2.rect.y -= 1
        if p2.face == "d":
            p2.rect.y += 1


def display_turn(screen, turn):
    """display_turn displays the owner of the turn

    This function displays the current turn on the screen, used
    for clarity of who gets to move.

    Arguments:
        screen (pygame.Surface): the screen we display the turn
            on
        turn (bool): a boolean indicating whether it's the
            player's turn or enemy's turn
    Returns:
        None.
    """
    if turn:
        s = "Your turn"
        c = (0,0,255)
    else:
        s = "Enemy Turn"
        c = (200,0,70)
    my_font = pygame.font.SysFont("monospace", 24)
    label = my_font.render(s,10,c)
    rect = pygame.Rect(10,10,210, 90)
    pygame.draw.rect(screen,(0,0,0), rect, 10)
    screen.fill((255,255,255), rect)
    screen.blit(label, (30, 30))


def display_moves(turn, p, p2, move, screen):
    """display_moves function, displays the moves of the
    selected character

    This function displays the moves of the selected character
    if it is the player's turn. Otherwise, it only indicates
    the current moves belong to the enemy.

    Arguments:
        turn (bool): indicates whether it's player turn
        p (Lord): the main character
        p2 (Cleric): the supporting character
        screen (pygame.Surface): the surface to draw the
            moves on
    Returns:
        None.
    """
    my_font = pygame.font.SysFont("monospace", 24)
    if not turn:
            label = my_font.render("Enemy move", 10,
                                   (200, 0, 70))
            rect = pygame.Rect(150, 600, 420, 90)
            pygame.draw.rect(screen, (0,0,0), rect, 10)
            screen.fill((255,255,255), rect)
            screen.blit(label, (180, 630))
    else:
        if p.selected:

            if p.c_move > 6:
                p.c_move = 6
            s = "Your move: " + str(p.c_move) + \
            " out of " + str(move) + " moves"
            label2 = my_font.render(s, 10, (0, 0, 255))
            rect = pygame.Rect(150, 600, 420, 90)
            pygame.draw.rect(screen, (0,0,0), rect, 10)
            screen.fill((255,255,255), rect)
            screen.blit(label2, (180, 630))
        elif p2.selected:
            if p2.c_move > 6:
                p2.c_move = 6
            s = "Your move: " + str(p2.c_move) + \
            " out of " + str(move) + " moves"
            label2 = my_font.render(s, 10, (0, 0, 255))
            rect = pygame.Rect(150, 600, 420, 90)
            pygame.draw.rect(screen, (0,0,0), rect, 10)
            screen.fill((255,255,255), rect)
            screen.blit(label2, (180, 630))


if __name__ == "__main__":

    main()