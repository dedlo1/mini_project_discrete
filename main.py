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
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.screen.fill(settings.WHITE)
            self.board.draw()
            pygame.display.update()
            self.clock.tick(settings.FPS)

if __name__ == '__main__':
    game = Game()
    game.run()
