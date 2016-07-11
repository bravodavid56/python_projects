import pygame


class SpriteSheet(object):
    """ Class used to grab images out of a sprite sheet.

    Attributes:
        None.
    """

    def __init__(self, file_name):
        """ intitializes the sprite sheet object

        This function loads the file indicated by the file name.

        Arguments:
            file_name (str): the name of the file containing
                the images
        """

        # Load the sprite sheet.
        self.sprite_sheet = pygame.image.load(file_name)\
            .convert_alpha()

    def get_image(self, x, y, width, height):
        """ get_image gets the image from the sprite sheet

        Gets the image at the specified x,y with the specified
        width and height

        Arguments:
            x (Int): x position of image
            y (Int): y position of image
            width (Int): width of the image
            height (Int): height of the image

        Returns:
            image (pygame.Surface): a surface containing the image

        """

        # Create a new blank image
        image = pygame.Surface([width, height]).convert()

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Assuming black works as the transparent color
        image.set_colorkey(pygame.Color("#80A080"))

        # Return the image
        return image
