'''
This is a script that has a class for board.
Bassicaly it's responsible for creating a map of our game
'''
import pygame
import settings
from tile import Tile

class Board:
    '''
    This a class that is responsible for drawing a board for our game
    '''
    def __init__(self) -> None:
        self.display_surface = pygame.display.get_surface()
        self.tiles = pygame.sprite.Group()
        self.create_board()

    def create_board(self):
        '''
        This method creates a board
        '''
        for y_ind, row in enumerate(settings.UCU_MAP):
            for x_ind, el in enumerate(row):
                x = x_ind * settings.TILESIZE
                y = y_ind * settings.TILESIZE
                if el == 'P':
                    Tile((x,y), './graphics/Podatkova.png', self.tiles)
                elif el == 'ß':
                    Tile((x,y), './graphics/center_shept.png', self.tiles)
                elif el == 'Ø':
                    Tile((x,y), './graphics/Canteene.png', self.tiles)
                elif el == 'C':
                    Tile((x,y), './graphics/Church.png', self.tiles)
                elif el == '1':
                    Tile((x,y), './graphics/K1.png', self.tiles)
                elif el == '0':
                    Tile((x,y), './graphics/K2_0.png', self.tiles)
                elif el == 'I':
                    Tile((x,y), './graphics/IT_space.png', self.tiles)
                elif el == '▓':
                    Tile((x,y), './graphics/park.png', self.tiles)
                elif el == 'V':
                    Tile((x,y), './graphics/vyshnya.png', self.tiles)

    def draw(self):
        '''
        This method draws a board created by create_board method
        '''
        self.tiles.draw(self.display_surface)
