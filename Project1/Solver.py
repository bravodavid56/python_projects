import pygame
from pygame.locals import *

screen_mode = (640, 480)
color_black = 0, 0, 0

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(screen_mode)
        pygame.display.set_caption("Pygame intro")
        self.quit = False

    def update(self):
        return

    def draw(self):
        self.screen.fill(color_black)
        pygame.display.flip()

    def mainLoop(self):
        while not self.quit:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.quit = True

            self.update()
            self.draw()

if __name__ == '__main__':
    game = Game()
    print("hello")
    game.mainLoop()
