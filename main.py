'''
This is the main file that has script to start the app
'''
import sys
import random
import pygame
import settings
from board import Board
from student_class import Student
from fsm import FSM
from ivents import Ivents, Pan_S

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
        self.machine = FSM()
        self.student_set = []
        self.unit_set = []

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
            self.spawn_student()

            if keys[pygame.K_1] and len(self.unit_set) == 0:
                self.unit_set.append(Pan_S((20, 10))
                )
                Ivents.pan_Stepan(self.student_set, self.unit_set[0])

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
            self.write_hotkeys()
            self.student_behavior()
            self.unit_behavior()
            pygame.display.update()
            self.clock.tick(settings.FPS)

    def write_hotkeys(self):
        '''
        This method writes hotkeys instructions in the window
        '''
        text_y = 18
        for line in settings.INSTRUCTIONS:
            img = pygame.font.SysFont('Arial', 16).render(line, True, settings.BLACK)
            self.screen.blit(img, (1260, text_y))
            text_y += 20

    def student_behavior(self):
        '''
        This method simulates student's behavior on the map (moving around)
        '''
        for num, std in enumerate(self.student_set):
            if std.will_to_live <= 8 and std.state[0] == "P":
                self.student_set.pop(num)
                continue
            if self.unit_set:
                std.dest = self.unit_set[0]
            self.machine.change_the_state(std)
            std.apply_the_state()
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
   
    def unit_behavior(self):
        '''
        This method simulates unit's behavior on the map (moving around)
        '''
        for _, unit in enumerate(self.unit_set):
            k = unit.move()
            if k:
                self.unit_set.pop(0)
                continue
            match unit.coords[1]:
                case 0:
                    unit.coords = (unit.coords[0], 1)
                case 69:
                    unit.coords = (unit.coords[0], 68)
            match unit.coords[0]:
                case 0:
                    unit.coords = (1, unit.coords[1])
                case 39:
                    unit.coords = (38, unit.coords[1])
            pygame.draw.rect(self.screen, [128, 0, 128],
                                (unit.coords[1]*settings.TILESIZE, unit.coords[0]*settings.TILESIZE,
                                settings.TILESIZE*2, settings.TILESIZE*2))

    def spawn_student(self):
        '''
        This method spawns a student on the coordinate of the cursor
        '''
        mouse_position = pygame.mouse.get_pos()
        spawn_y = mouse_position[1]//18
        spawn_x = mouse_position[0]//18
        if spawn_x >= 69:
            spawn_x = 68
        if pygame.mouse.get_pressed()[0]:
            self.student_set.append(Student(random.randrange(35, 50),
                                            random.randrange(0, 50),
                                            (spawn_y, spawn_x)))

if __name__ == '__main__':
    game = Game()
    game.run()
