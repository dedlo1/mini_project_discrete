import settings
from student_class import Park, Student, Canteene


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
            student.will_to_live -= 5
            student.chance_to_fail -= 5

    @staticmethod
    def Oles(student_set):
        """
        Increase will_to_live by 5
        """
        for student in student_set:
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

import random
from student_class import Student


class Pan_S(Student):
    def __init__(self, coords):
        super().__init__(50, 0, coords)

    def move(self):


        if self.dest is None:
            self.set_new_destination(Park())


        elif self.boredom >= 10:
            self.set_new_destination(Canteene())
            self.boredom = 0

        elif self.coords in self.dest:

            if isinstance(self.dest, Park):
                self.move_inside()
                self.boredom += 1


            elif isinstance(self.dest, Canteene):
                return True

        if not self.path:
            self.grid_bfs()

        self.coords = self.path.pop(0)


    def __contains__(self, coords):
        return self.coords[0] <= coords[0] <= self.coords[0] + 2 and self.coords[1] <= coords[1] <= self.coords[1] + 2
