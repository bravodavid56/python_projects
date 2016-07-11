import pygame


class Card(pygame.sprite.Sprite):
    """The Card class is a sprite representative of a
    playing card.

    Attributes:
        None.
    """
    def __init__(self, x, y, vx, vy, c=0):
        """Constructor for the Card class.

         Takes in several parameters, to create a moving card
         across the window.

         Arguments:
            x (Int): the x value for the rectangle surrounding the
                sprite.
            y (Int): the y value for the rectangle surrounding the
                sprite.
            vx (Int): the velocity on the x-axis of the card
            vy (Int): the velocity on the y-axis of the card
            c (Int): used to indicate a black or red card (0, 1)
        """
        super().__init__()
        if c == 0:
            self.image = pygame.image.load("c01.png").convert_alpha()
        else:
            self.image = pygame.image.load("h01.png").convert_alpha()

        self.image.set_colorkey(pygame.Color(0, 0, 0))

        self.rect = self.image.get_rect()

        self.rect.x = x
        self.rect.y = y
        self.vx = vx
        self.vy = vy

    def draw(self, SCREEN):
        """draw method, draws the card on top of the screen

        Draws this instance of a card on top of the screen.

        Arguments:
            SCREEN (pygame.display): the canvas for drawing
        Returns:
            None.
        """
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

    def move(self, sw, sh, block_list):
        """move method, moves the card based on collisions

        The move method attempts to move the card in the direction
        and speed indicated by vx and vy, unless there is a
        collision, in which case it reverses the direction
        by checking the card against the cards in the
        block_list.

        Arguments:
            sw (Int): the width of the screen
            sh (Int): the height of the screen
            block_list (pygame.sprite.Group): a group of the sprites
                in the game; used for collision detection
        Returns:
            None.
        """
        block_list.remove(self)

        r_collide = False
        l_collide = False
        t_collide = False
        b_collide = False

        b = self.get_boundaries()

        if b[0] > sw:
            r_collide = True
        if b[1] < 0:
            l_collide = True
        if b[2] < 0:
            t_collide = True
        if b[3] > sh:
            b_collide = True

        cs = pygame.sprite.spritecollide(self, block_list, False)

        for s in cs:
            s.vx *= -1
            s.vy *= -1

        block_list.add(self)

        # Check collision on right and left sides of screen
        if l_collide or r_collide:
            self.vx *= -1

        # Check collision on top and bottom sides of screen
        if t_collide or b_collide:
            self.vy *= -1

        self.rect.x += self.vx
        self.rect.y += self.vy

    def get_boundaries(self):
        """get_boundaries method, returns the boundaries for the card

        This function is called in the move() function for collision
        detection. Using the surrounding rectangle, and
        the velocity, this function calculates the right, left, top,
        and bottom boundary for the card.

        Arguments:
            None.
        Returns:
            list: Returns a list of the boundaries in order of
                right, left, top, and bottom
        """
        rb = self.rect.x + self.image.get_width() + self.vx
        lb = self.rect.x + self.vx
        tb = self.rect.y + self.vy
        bb = self.rect.y + self.image.get_height() + self.vy
        boundaries = [rb, lb, tb, bb]
        return boundaries

    def update(self, *args):
        """update function, called on each time the sprite is updated.

        This function is called every time the group's update function
        is called, using function mapping.

        Arguments:
            *args (Int, Int, pygame.sprite.Group): takes in a list
                containing the width of the screen, the height, and
                the group of sprites.
         Returns:
             None.
        """
        self.move(args[0], args[1], args[2])
