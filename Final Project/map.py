import pygame


class Map1(pygame.sprite.Sprite):
    """A map representing the map used in the game

    Attributes:
        None.
    """
    def __init__(self):
        """initializes the Map object

        This function initializes the Map object to a specified
        image.

        Arguments:
            None.
        """
        super().__init__()
        self.image = pygame.image.load("map1.jpg").convert_alpha()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()

    def draw(self, SCREEN):
        """draws the map image on the screen

        This function draws the map image on the screen.

        Arguments:
            SCREEN (pygame.Surface): where to draw the map
        """
        SCREEN.blit(self.image, (0, 0))
