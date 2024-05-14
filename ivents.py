import pygame
import settings
import random
from student_class import Park, Student, Canteene
from special_units_waypoints import (StepanWaypoint1, StepanWaypoint2, StepanWaypoint3,
                                  StepanWaypoint4, StepanWaypoint5, StepanWaypoint6,
                                  StepanWaypoint7, StepanWaypoint8, StepanWaypoint9,
                                  OlesWaypoint1)

TIMER_TEMPLATE = [False]*25
TIMER_TEMPLATE.append(True)

class Ivents:
    """
    This class is responsible for the events that can happen to the student
    """

    @staticmethod
    def pan_Stepan(student_set, coords):
        """
        Increase will_to_live by 5
        Decrease chance_to_fail by 5
        """
        for student in student_set:
            student.dest = coords
            student.will_to_live += 5
            student.chance_to_fail -= 5

    @staticmethod
    def cos_pT(student_set):
        """
        Decrease will_to_live by 5
        Decrease chance_to_fail by 3
        """
        for student in student_set:
            student.will_to_live -= 5
            student.chance_to_fail -= 3

    @staticmethod
    def cos_pY(student_set):
        """
        Decrease will_to_live by 5
        Increase chance_to_fail by 7
        """
        for student in student_set:
            student.chance_to_fail -= 5

    @staticmethod
    def Oles(student_set, coords):
        """
        Increase will_to_live by 5
        """
        for student in student_set:
            student.dest = coords
            student.will_to_live += 5

    @staticmethod
    def povers(student_set):
        """
        Increase chance_to_fail by 5
        """
        for student in student_set:
            student.chance_to_fail += 5

    @staticmethod
    def ispyt(student_set):
        """
        In order to chance_to_fail delete the student from the set
        """
        set_copy = student_set.copy()
        for student in set_copy:
            if student.chance_to_fail >= 40:
                student_set.remove(student)

class Pan_S(Student):
    def __init__(self, coords):
        super().__init__(50, 0, coords)

    def move(self):

        if self.dest is None:
            self.set_new_destination(Park())

        elif self.coords in self.dest:

            if isinstance(self.dest, Park):
                self.set_new_destination(StepanWaypoint1())

            elif isinstance(self.dest, StepanWaypoint1):
                self.set_new_destination(StepanWaypoint2())

            elif isinstance(self.dest, StepanWaypoint2):
                self.set_new_destination(StepanWaypoint3())

            elif isinstance(self.dest, StepanWaypoint3):
                self.set_new_destination(StepanWaypoint4())

            elif isinstance(self.dest, StepanWaypoint4):
                self.set_new_destination(StepanWaypoint5())

            elif isinstance(self.dest, StepanWaypoint5):
                self.set_new_destination(StepanWaypoint6())

            elif isinstance(self.dest, StepanWaypoint6):
                self.set_new_destination(StepanWaypoint7())

            elif isinstance(self.dest, StepanWaypoint7):
                self.set_new_destination(StepanWaypoint8())

            elif isinstance(self.dest, StepanWaypoint8):
                self.set_new_destination(StepanWaypoint9())

            elif isinstance(self.dest, StepanWaypoint9):
                self.set_new_destination(Canteene())

            elif isinstance(self.dest, Canteene):
                return True

        if not self.path:
            self.grid_bfs()

        self.coords = self.path.pop(0)


    def __contains__(self, coords):
        return (self.coords[0] <= coords[0] <= self.coords[0] + 2 and
                self.coords[1] <= coords[1] <= self.coords[1] + 2)

class Oles(Student):
    def __init__(self, coords, screen):
        super().__init__(50, 0, coords)
        self.screen = screen
        self.timer = iter(TIMER_TEMPLATE)

    def start_picnic(self):
        pygame.draw.rect(self.screen, (242, 215, 61),
                            ((self.coords[1]-2)*settings.TILESIZE, (self.coords[0]-2)*settings.TILESIZE,
                            settings.TILESIZE*6, settings.TILESIZE*6))

    def move(self):

        if self.dest is None:
            self.set_new_destination(OlesWaypoint1())

        elif self.coords in self.dest:

            if isinstance(self.dest, OlesWaypoint1):
                self.start_picnic()
                if next(self.timer):
                    self.set_new_destination(Canteene())
                # self.set_new_destination(Canteene())

            elif isinstance(self.dest, Canteene):
                return True

        if not self.path:
            self.grid_bfs()

        self.coords = self.path.pop(0)


    def __contains__(self, coords):
        return (self.coords[0] <= coords[0] <= self.coords[0] + 2 and
                self.coords[1] <= coords[1] <= self.coords[1] + 2)
