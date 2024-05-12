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
                self.student_set.append(Student(random.randrange(35, 50),
                                             random.randrange(0, 50),
                                             (random.randrange(1, 39),
                                              random.randrange(1,69))))
            self.screen.fill(settings.WHITE)
            self.board.draw()
            self.student_behavior()
            pygame.display.update()
            self.clock.tick(settings.FPS)

    def student_behavior(self):
        '''
        This method simulates student's behavior on the map (moving around)
        '''
        for num, std in enumerate(self.student_set):
            if std.will_to_live <= 5 and std.state[0] == "P":
                print(f"Deleted {std}")
                self.student_set.pop(num)
                continue
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


if __name__ == '__main__':
    game = Game()
    game.run()
    # st = Student(10, 100, (12, 62))
    # st.state = ["V", (0, 0)]
    # m = FSM()
    # print(st)
    # m.change_the_state(st)
    # st.apply_the_state()
    # print(st)
    # print(st.color)
    # m.change_the_state(st)
    # st.apply_the_state()
    # print(st)
    # print(st.color)
    # # print(st)