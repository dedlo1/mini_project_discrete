import random
import pygame
import settings
from board import Board
from student_class import Student
from turing_machine import TuringMachine


class Ivents:
    """
    This class is responsible for the events that can happen to the student
    """

    @staticmethod
    def pan_Stepan(student_set):
        """
        Increase will_to_live by 5
        Decrease chance_to_fail by 5
        """
        for student in student_set:
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
            student.chance_to_fail += 7

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
