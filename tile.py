'''
This file has a tile class
'''
import pygame

class Tile(pygame.sprite.Sprite):
    '''
    This is a class that represents a tile on the map
    '''
    def __init__(self, pos, image_path, groups) -> None:
        super().__init__(groups)
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
