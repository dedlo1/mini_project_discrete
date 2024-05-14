'''
This is script contains classes for Pan Stepan road.
It's a bruteforce way to do it but it's fine
'''

class StepanWaypoint1:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 32 <= coords[0] <= 34 and 58 <= coords[1] <= 60

class StepanWaypoint2:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 31 <= coords[0] <= 34 and 66 <= coords[1] <= 68

class StepanWaypoint3:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 17 <= coords[0] <= 19 and 65 <= coords[1] <= 67

class StepanWaypoint4:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 15 <= coords[0] <= 16 and 52 <= coords[1] <= 53

class StepanWaypoint5:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 24 <= coords[0] <= 25 and 52 <= coords[1] <= 53

class StepanWaypoint6:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 24 <= coords[0] <= 25 and 41 <= coords[1] <= 42

class StepanWaypoint7:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 9 <= coords[0] <= 10 and 41 <= coords[1] <= 42

class StepanWaypoint8:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 8 <= coords[0] <= 9 and 17 <= coords[1] <= 18

class StepanWaypoint9:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 17 <= coords[0] <= 18 and 17 <= coords[1] <= 18

class OlesWaypoint1:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 3 <= coords[0] <= 4 and 19 <= coords[1] <= 20

class PaniTetyanaWaypoint1:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 8 <= coords[0] <= 9 and 28 <= coords[1] <= 29

class PaniTetyanaWaypoint2:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 9 <= coords[0] <= 10 and 17 <= coords[1] <= 18
    
class PaniTetyanaWaypoint3:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 26 <= coords[0] <= 27 and 17 <= coords[1] <= 18

class PaniYuliaWaypoint1:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 3 <= coords[0] <= 4 and 46 <= coords[1] <= 47

class PaniYuliaWaypoint2:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 4 <= coords[0] <= 5 and 37 <= coords[1] <= 38

class PaniYuliaWaypoint3:
    '''
    This is a class of Waypoint for Pan Stepan event
    '''
    def __init__(self):
        self.will_to_live = 0
        self.chance_to_fail = 0

    def __contains__(self, coords):
        return 37 <= coords[0] <= 38 and 49 <= coords[1] <= 50
