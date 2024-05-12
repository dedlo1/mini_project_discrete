'''
This is the main file that has script to start the app
'''
import sys
import random
import pygame
import settings
from board import Board
from student_class import Student
from turing_machine import TuringMachine
from ivents import Ivents

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
        self.machine = TuringMachine()
        self.student_set = set()

    def run(self):
        '''
        This method is responsible for creating and running a window
        '''
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_s]:
                self.student_set.add(Student(random.randrange(35, 50),
                                             random.randrange(0, 50),
                                             (random.randrange(1, 39),
                                              random.randrange(1,69))))
            if keys[pygame.K_1]:
                Ivents.pan_Stepan(self.student_set)
                # write text on the screen
                # font = pygame.font.Font('freesansbold.ttf', 32)
                # text = font.render("Pan S", True, settings.BLACK)
                # self.screen.blit(text, (10, 10))


            if keys[pygame.K_2]:
                Ivents.cos_pT(self.student_set)
            if keys[pygame.K_3]:
                Ivents.cos_pY(self.student_set)
            if keys[pygame.K_4]:
                Ivents.Oles(self.student_set)
            if keys[pygame.K_5]:
                Ivents.povers(self.student_set)
            if keys[pygame.K_6]:
                Ivents.ispyt(self.student_set)

            self.screen.fill(settings.WHITE)
            self.board.draw()
            self.student_behavior()
            pygame.display.update()
            self.clock.tick(settings.FPS)

    def student_behavior(self):
        '''
        This method simulates student's behavior on the map (moving around)
        '''
        for std in self.student_set:
            self.machine.apply_the_rules(std)
            std.move()
            match std.coords[1]:
                case 0:
                    std.coords = (std.coords[0], 1)
                case 69:
                    std.coords = (std.coords[0], 68)
            match std.coords[0]:
                case 0:
                    std.coords = (1, std.coords[1])
                case 39:
                    std.coords = (38, std.coords[1])
            pygame.draw.rect(self.screen, std.color,
                                (std.coords[1]*settings.TILESIZE, std.coords[0]*settings.TILESIZE,
                                settings.TILESIZE, settings.TILESIZE))


if __name__ == '__main__':
    game = Game()
    game.run()
