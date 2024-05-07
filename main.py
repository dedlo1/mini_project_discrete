'''
This is the main file that has script to start the app
'''
import sys
import pygame
import settings
from board import Board

class Game:
    '''
    This is the game class which is responsible with initializing a game screen 
    and starting a game itself
    '''
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption('Da game')
        self.screen = pygame.display.set_mode((settings.WIDTH, settings.HEIGHT))
        self.clock = pygame.time.Clock()
        self.board = Board()

    def run(self):
        '''
        This method is responsible for creating and running a window
        '''
        # x = 18
        # y = 18
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(settings.WHITE)
            self.board.draw()
            # This was a testing of creating a sprite without influencing the map
            # keys = pygame.key.get_pressed()
            # if keys[pygame.K_LEFT]:
            #     x -= 18
            # if keys[pygame.K_RIGHT]:
            #     x += 18
            # if keys[pygame.K_UP]:
            #     y -= 18
            # if keys[pygame.K_DOWN]:
            #     y += 18
            # pygame.draw.rect(self.screen, (255, 150, 180), (x, y, 18, 18))
            pygame.display.update()
            self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
