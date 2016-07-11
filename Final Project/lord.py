import pygame
from unit import Unit
from sprite_sheet import SpriteSheet


class Lord(Unit):
    """the main character, derived from Unit

    This class represents the main character.

    Attributes:
        stand_f (list): a list of the standing frames
        selected_f (list): a list of the selected frames
        walking_l_f (list): a list of walking left frames
        walking_r_f (list): a list of walking right frames
        walking_u_f (list): a list of walking up frames
        walking_d_f (list): a list of walking down frames
    """

    # standing frames
    stand_f = []

    selected_f = []

    # walking left, right frames
    walking_l_f = []
    walking_r_f = []

    # walking up, down frames
    walking_u_f = []
    walking_d_f = []

    def __init__(self, ss, w, x=0, y=0):
        """initializes the Lord object

        This function initializes the Lord object with some
        default values, such as a face, and selected.

        Arguments:
            ss (SpriteSheet): a spritesheet containing standing
            w (SpriteSheet): a spritesheet containing walking
            x (Int): x position of the Lord
            y (Int): y position of the Lord
        """
        super().__init__()
        # place player's sprite here
        self.ss = SpriteSheet(ss)
        self.w = SpriteSheet(w)

        ss = self.ss
        w = self.w

        self.stand_frames(ss)
        self.left_frames(w)
        self.right_frames()
        self.up_frames(w)
        self.down_frames(w)
        self.selected_frames(w)

        self.image = self.stand_f[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.c_move = 0
        self.hp = 25
        self.mhp = 0

        self.selected = True
        self.face = "n"
        self.done = False

    def update(self, *args):
        """update function used in pygame.Sprite.Group

        This function is called automatically at each update
        in the main game loop. This function asserts which way
        the Lord moves based on the direction faced, and
        updates the health bar.

        Arguments:
            *args (Int): index of the frame
        Returns:
            None.
        """
        if self.selected:
            if self.face == "l":
                self.image = self.walking_l_f[args[1]]
                self.move("l")
            if self.face == "r":
                self.image = self.walking_r_f[args[1]]
                self.move("r")
            if self.face == "u":
                self.image = self.walking_u_f[args[1]]
                self.move("u")
            if self.face == "d":
                self.image = self.walking_d_f[args[1]]
                self.move("d")
            if self.face == "n":
                self.image = self.selected_f[args[1]]
        else:
            if self.face == "s":
                self.image = self.stand_f[args[1]]

        if self.selected:
            rect = pygame.Rect(1,1,5,5)
            self.image.fill((255,255,255), rect)
        elif self.done:
            rect = pygame.Rect(1,1,5,5)
            self.image.fill((0,0,0), rect)
        elif not self.selected and not self.done:
            rect = pygame.Rect(1,1,5,5)
            self.image.fill((0,255,0), rect)
        if self.mhp > 0:
            rect = pygame.Rect(1,20,self.hp, 5)
            self.image.fill((0,255,0), rect)
            rect = pygame.Rect(1,20,self.mhp, 5)
            self.image.fill((255,0,0), rect)
        else:
            rect = pygame.Rect(1,20,self.hp, 5)
            self.image.fill((0,255,0), rect)

    def move(self, face):
        """move function decides movement

        This function defines where, how, and when to move
        a Lord object; also updates the "done" property to
        disable further movements.

        Arguments:
            face (str): the direction faced by the Lord
        """
        if self.c_move >= 6:
            self.done = True
            self.selected = False
            self.face = "s"
        else:
            if face == "r":
                if self.rect.x + 10 <= 720 and \
                        self.rect.y >= 180:
                    self.rect.x += 10
                elif self.rect.x + 10 <= 420 and \
                        self.rect.y <= 180:
                    self.rect.x += 10
                elif 480<=self.rect.x+10<=720 and\
                    0<=self.rect.y<=90:
                    self.rect.x += 10
            if face == "l":
                if self.rect.x - 10 >= 0 and \
                        self.rect.y >= 180:
                    self.rect.x -= 10
                elif 420>=self.rect.x -10>=300:
                    self.rect.x -= 10
                elif 480 < self.rect.x - 10 < 720 and \
                        0 <= self.rect.y <= 90:
                    self.rect.x -= 10
            if face == "u":
                if self.rect.y - 10 >= 180 and \
                        self.rect.x >= 300:
                    self.rect.y -= 10
                elif self.rect.y - 10 >= 0 and \
                    300<=self.rect.x<=420:
                    self.rect.y -= 10
                elif self.rect.y - 10 >= 0 and \
                    self.rect.x == 600:
                    self.rect.y -= 10
                elif 0<self.rect.y<=90 and \
                    480 <= self.rect.x <= 720:
                    self.rect.y -= 10
            if face == "d":
                if 180<=self.rect.y + 10 <= 720:
                    self.rect.y += 10
                elif self.rect.y +10 <=720 and \
                    300<=self.rect.x<=420:
                    self.rect.y += 10
                elif 0<self.rect.y+10<=90 and \
                    480<=self.rect.x<=720:
                    self.rect.y += 10
                elif self.rect.y +10 <=720 and \
                    self.rect.x == 600:
                    self.rect.y += 10
        self.c_move += 1

    def stand_frames(self, ss):
        """instantiates the frames for standing

        Takes the frames for standing from the indicated
        spritesheet

        Arguments:
            ss (SpriteSheet): a spritesheet for standing frames
        Returns:
            None.
        """
        # image height, width
        ssh = 16
        ssw = 20
        ssht = int(16*1.5)
        sswt = int(20*1.5)

        # standing image frames
        image = ss.get_image(0, 12, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.stand_f.append(image)
        image = ss.get_image(0, 44, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.stand_f.append(image)
        image = ss.get_image(0, 75, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.stand_f.append(image)
        self.stand_f.append(image)
        self.stand_f.append(image)
        image = ss.get_image(0, 44, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.stand_f.append(image)
        image = ss.get_image(0, 12, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.stand_f.append(image)

    def selected_frames(self, w):
        """instantiates the frames for selected

        Takes the frames for selected from the indicated
        spritesheet

        Arguments:
            w (SpriteSheet): a spritesheet for selected frames
        Returns:
            None.
        """
        image = w.get_image(0, 388, 32, 26)
        self.selected_f.append(image)
        image = w.get_image(0, 421, 32, 28)
        self.selected_f.append(image)
        image = w.get_image(0, 454, 32, 28)
        self.selected_f.append(image)

    def left_frames(self, w):
        """instantiates the frames for walking left

        Takes the frames for walking left from the indicated
        spritesheet

        Arguments:
            w (SpriteSheet): a spritesheet for walking frames
        Returns:
            None.
        """
        # walking left frames
        ssht = (int)(28*1.3)
        sswt = (int)(28*1.3)
        image = w.get_image(0, 0, 28, 32)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_l_f.append(image)
        image = w.get_image(0, 39, 32, 26)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_l_f.append(image)
        image = w.get_image(0, 70, 32, 26)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_l_f.append(image)
        image = w.get_image(0, 70, 32, 26)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_l_f.append(image)
        image = w.get_image(0, 39, 32, 26)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_l_f.append(image)

    def right_frames(self):
        """reverses the frames in walking_l_f, sets to walking_r_f

        Reverses the frames in the walking left list, and assigns
        to walking right list.

        Arguments:
            None.
        Returns:
            None.
        """
        # walking right frames
        self.walking_r_f = [pygame.transform.flip(i, True, False)
                            for i in self.walking_l_f]

    def up_frames(self, w):
        """instantiates the frames for walking right

        Takes the frames for walking right from the indicated
        spritesheet

        Arguments:
            w (SpriteSheet): a spritesheet for walking frames
        Returns:
            None.
        """
        # walking up frames
        ssh = 32
        ssw = 26

        ssht = (int)(32*1.1)
        sswt = (int)(26*1.1)

        image = w.get_image(0, 264, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_u_f.append(image)
        image = w.get_image(0, 297, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_u_f.append(image)
        image = w.get_image(0, 328, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_u_f.append(image)
        image = w.get_image(0, 360, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_u_f.append(image)

    def down_frames(self, w):
        """instantiates the frames for walking down

        Takes the frames for walking down from the indicated
        spritesheet

        Arguments:
            w (SpriteSheet): a spritesheet for walking frames
        Returns:
            None.
        """
        # walking down frames
        ssh = 32
        ssw = 26

        ssht = (int)(32*1.1)
        sswt = (int)(26*1.1)

        image = w.get_image(0, 133, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_d_f.append(image)
        image = w.get_image(0, 165, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_d_f.append(image)
        image = w.get_image(0, 196, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_d_f.append(image)
        image = w.get_image(0, 229, ssh, ssw)
        image = pygame.transform.scale(image,(ssht,sswt))
        self.walking_d_f.append(image)






