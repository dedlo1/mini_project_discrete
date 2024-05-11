"""Player class"""
import random
from numpy.random import choice
from fsm import dict_of_rules


def make_the_colors() -> list:
    """
    Make the colors as a list. Elements stare from dark to light!!
    Red : 2nd index
    Blue : 1st index
    Green : 0 index
    """
    shades = [[], [], []]
    for intensity in range(0, 255, 10):
        shades[2].append((intensity, 0, 0))
        shades[0].append((0, intensity, 0))
        shades[1].append((0, 0, intensity))
    return shades

LIST_OF_COLORS = make_the_colors()

def plot_the_colors() -> None:
    """Call the function to see the colors"""
    import matplotlib.pyplot as plt
    sh = make_the_colors()
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 3, 1)
    plt.imshow([sh[2]], aspect='auto')
    plt.title('Shades of Red')
    plt.axis('off')

    plt.subplot(1, 3, 3)
    plt.imshow([sh[1]], aspect='auto')
    plt.title('Shades of Blue')
    plt.axis('off')

    plt.subplot(1, 3, 2)
    plt.imshow([sh[0]], aspect='auto')
    plt.title('Shades of Green')
    plt.axis('off')

    plt.tight_layout()
    plt.show()


class Student:
    """APPS student"""
    def __init__(self, will_to_live:int, chance_to_fail:int, coords) -> None:
        """Initializing the attributes"""
        self.will_to_live = will_to_live
        self.chance_to_fail = chance_to_fail
        self.boredom = 0
        self.coords = coords
        self.path = []
        self.dest = None
        self.state = [None, (0, 0)]
        self.special_state = None

    def __repr__(self) -> str:
        return f"Student: {self.will_to_live}, {self.chance_to_fail}"

    def apply_the_state(self):
        if self.special_state:
            self.chance_to_fail -= 2
        self.will_to_live += self.state[1][0]
        self.chance_to_fail += self.state[1][1]
        


    def move(self):
        '''
        Move the student.
        '''

        self.boredom += 1
        urgency = (50 - self.will_to_live) + self.chance_to_fail + self.boredom

        if random.random() + urgency * 0.01 > 0.9:
            self.choose_destination()
            self.boredom = 0

        if self.dest is None:
            self.choose_random_path()

        else:
            self.move_to_destination()


    def set_new_destination(self, destination):
        '''
        Manually set a new destination for the student.
        '''

        self.dest = destination
        self.path = []


    def set_new_path(self, path):
        '''
        Manually set a new path for the student.
        '''

        self.path = path


    def choose_destination(self):
        '''
        Choose the destination that the student will go to.
        '''

        possibilities = sorted(dict_of_rules)

        probabilities = [
            max(0, (dict_of_rules[key][0] * (50 - self.will_to_live) - dict_of_rules[key][1] * self.chance_to_fail))
            for key in possibilities
        ]

        divid = sum(probabilities)

        if divid:
            probabilities = [p / divid for p in probabilities]
    
        else:
            probabilities = [1 / len(probabilities) for _ in probabilities]

        result = choice(possibilities, None, True, probabilities)

        self.dest = sign_t0_class[result]()


    def choose_random_path(self):
        '''
        Choose a random path for the student. Used if there is no destination.
        '''

        dy, dx = random.choice(((0, 1), (1, 0), (-1, 0), (0, -1)))
        self.coords = (self.coords[0] + dy, self.coords[1] + dx)


    def move_inside(self):
        '''
        Move the student inside the building.
        Used when the student reaches the current destination.
        '''
        possibilities = []

        for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):

            new_coords = (self.coords[0] + dy, self.coords[1] + dx)

            if self.dest is not None and new_coords in self.dest:
                possibilities.append(new_coords)

        self.coords = random.choice(possibilities)


    def move_to_destination(self):
        '''
        Move the student to the destination, or inside the destination.
        '''
        if self.will_to_live < 15:
            self.set_new_destination(Podatkova())

        if self.dest is not None and self.coords in self.dest:
            self.move_inside()
            return

        elif not self.path:
            self.grid_bfs()

        self.coords = self.path.pop(0)


    def grid_bfs(self):
        """
        Breadth-first search on a grid, decides on the best path to the destination
        """
        visited = {self.coords}
        queue = [[self.coords]]
        while queue:
            current = queue.pop(0)
            for dy, dx in ((0, 1), (1, 0), (-1, 0), (0, -1)):
                new_coords = (current[-1][0] + dy, current[-1][1] + dx)
                if self.dest is not None and new_coords in self.dest:
                    self.path = current[1:] + [new_coords]
                    return
                if 1 <= new_coords[0] <= 38 and 1 <= new_coords[1] <= 68 and new_coords not in visited:
                    visited.add(new_coords)
                    queue.append(current + [new_coords])


    @property
    def color(self):
        """
        Student's color
        I assume that the max of each attribute can reach up to 50
        """
        print("None" if not self.special_state else str(self.special_state))
        # print(self.will_to_live//2 - 1)
        if self.special_state:
            print("hi")
            return (128, 0, 128)
        else:
            if self.chance_to_fail >= 34:
                color_index = 2
            elif self.chance_to_fail >= 17:
                color_index = 1
            else:
                color_index = 0
            if self.will_to_live > 50:
                return LIST_OF_COLORS[color_index][24]
            if self.will_to_live < 0:
                return LIST_OF_COLORS[color_index][0]
            return LIST_OF_COLORS[color_index][self.will_to_live//2 - 1]


class Podatkova:
    '''
    Podatkova building
    '''

    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 1 <= coords[0] <= 7 and 1 <= coords[1] <= 10


class Shept:
    '''
    Sheptytskyi building
    '''

    def __init__(self):
        self.will_to_live = -1
        self.chance_to_fail = -1

    def __contains__(self, coords):
        return (1 <= coords[0] <= 7 and 35 <= coords[1] <= 50) or\
                (8 <= coords[0] <= 22 and 44 <= coords[1] <= 50)


class Church:
    '''
    Church building
    '''

    def __init__(self):
        self.will_to_live = 1
        self.chance_to_fail = -1

    def __contains__(self, coords):
        return 11 <= coords[0] <= 13 and 62 <= coords[1] <= 64


class Park:
    '''
    Park
    '''

    def __init__(self):
        self.will_to_live = 1
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 1 <= coords[0] <= 38 and 55 <= coords[1] <= 68 and\
            not (11 <= coords[0] <= 13 and 62 <= coords[1] <= 64)


class PV:
    '''
    PV building
    '''

    def __init__(self):
        self.will_to_live = 5
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 11 <= coords[0] <= 13 and 62 <= coords[1] <= 64


class Canteene:
    '''
    Canteene
    '''
    
    def __init__(self):
        self.will_to_live = 1
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 12 <= coords[0] <= 22 and 5 <= coords[1] <= 14


class K1:
    '''
    K1 building
    '''
    
    def __init__(self):
        self.will_to_live = 1
        self.chance_to_fail = -1

    def __contains__(self, coords):
        return (28 <= coords[0] <= 31 and 22 <= coords[1] <= 44) or\
                (31 <= coords[0] <= 34 and 38 <= coords[1] <= 44)


class K2:
    '''
    K2 building
    '''

    def __init__(self):
        self.will_to_live = 2
        self.chance_to_fail = 2

    def __contains__(self, coords):
        return 35 <= coords[0] <= 38 and 22 <= coords[1] <= 44


class IT:
    '''
    IT building
    '''
    
    def __init__(self):
        self.will_to_live = -2
        self.chance_to_fail = -2

    def __contains__(self, coords):
        return 23 <= coords[0] <= 30 and 5 <= coords[1] <= 14

# class Zahublenie:
#     """You got lost in piana vyshnia"""
#     def __init__(self) -> None:
#         self.will_to_live = 0
#         self.chance_to_fail = 2


sign_t0_class = {'P': Podatkova, 'ß': Shept, 'C': Church, '1': K1, '0': K2, 'I': IT, 'V': PV, 'Ø': Canteene, '▓': Park}
