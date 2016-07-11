import pygame
from card import Card
from pygame.locals import *
import sys
import random
"""solitaire_animation module -- Implements colliding Card sprites.

This module creates sprites in the shape of playing cards,
and uses collision detection when adding multiple cards.
The user can choose to add cards, or subtract them.

Note:
    Use '+' key to add a card. If this does not work,
        use a different keyboard, or the '+' on a
        number pad, not the '+' key next to
        backspace -- unsure of why this specification
        is necessary.
    Use '-' key to subtract the last instance of a card.
        Again, if this does not work, try other '-' keys,
        either on a different keyboard or on a number
        pad.

    Run the program from the command line:
        $ python solitaire_animation.py

Attribute(s):
    None.
"""

def main():
    """main function, creates the window and houses the
    game loop.

    This function creates the window, and initiates the
    running game loop. It creates cards on key press,
    and removes them on key press.

    Arguments:
        None.

    Returns:
        None.
    """
    pygame.init()

    FPS = 30
    FPS_CLOCK = pygame.time.Clock()

    GREEN = pygame.Color(41, 135, 55)

    sw = 750
    sh = 750
    window_size = (sw, sh)
    SCREEN = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Successful Solitaire Animation")

    SCREEN.fill(GREEN)

    block_list = pygame.sprite.Group()
    last_added = pygame.sprite.Group.sprites(block_list)

    red = False
    card = create_card(sw, sh, red)
    add_card(block_list, card)
    red = True
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYUP:
                if event.key == K_KP_MINUS:
                    remove_card(block_list,
                                last_added)
                if event.key == K_KP_PLUS:
                    card = create_card(sw, sh, red)
                    add_card(block_list, card)
                    red = not red
                    last_added.append(card)

        SCREEN.fill(GREEN)
        block_list.update(sw, sh, block_list)

        block_list.draw(SCREEN)

        pygame.display.flip()
        FPS_CLOCK.tick(FPS)


def add_card(block_list, card):
    """add_card function -- adds a card to the group of sprites.

    This function adds a card to the group of sprites in the program.
    Note, this function is added here more for visibility than for
    necessity, given it is only one line of code.

    Arguments:
        block_list (pygame.sprite.Group): a group of the sprites
        card (Card): a card to be added to the group of sprites
    Returns:
        None.
    """
    block_list.add(card)


def remove_card(block_list, last_added):
    """remove_card function -- removes the last instance of the card

    This function removes the last instance of an added card using a
    last_added list which keeps track of the order in which cards are
    added. It then removes the card from the block_list group of sprites,
    and from the list indicating the order in which the cards were added.

    Arguments:
        block_list (pygame.sprite.Group): a group of sprites
        last_added (list): a list keeping track of order of added cards
    Returns:
        None.
    """
    if len(last_added) > 0:
        block_list.remove(last_added[len(last_added)-1])
        del last_added[len(last_added)-1]


def create_card(sw, sh, c):
    """create_card function -- creates an instance of Card and returns it

    This function creates an instance of a Card using the screen width
    and height to ensure it is created in bounds. It also takes in 'c'
    which is used for indicating whether it is a red card or a black card.

    Arguments:
        sw (Int): the width of the screen
        sh (Int): the height of the screen
        c (Int): either 0 or 1, used for color of card
     Returns:
         Card: Returns an instance of Card.
    """
    if not c:
        card = Card(random.randrange(sw), random.randrange(sh),
                    random.randrange(10)+1, random.randrange(10)+1)
    else:
        card = Card(random.randrange(sw), random.randrange(sh),
                    random.randrange(10)+1, random.randrange(10)+1,1)
    if card.rect.x > sw - 90:
        card.rect.x -= 90
    if card.rect.y > sh - 125:
        card.rect.y -= 125
    return card

if __name__ == "__main__":
    main()
