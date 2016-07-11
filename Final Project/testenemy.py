import pygame


class TestE(pygame.sprite.Sprite):
    def __init__(self, x, y, hp, move, str):
        super().__init__()
        self.image.set_colorkey(pygame.Color(0,0,0))
        self.rect = self.image.get_rect()

    def draw(self, SCREEN):
        SCREEN.blit(self.image, (0, 0))

        rect = pygame.Rect(390,390, 27, 27)
        pygame.draw.rect(SCREEN, pygame.Color(255,255,255),
                           rect, 0)
