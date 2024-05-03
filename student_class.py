"""Player class"""
def make_the_colors() -> list:
    """
    Make the colors as a list. Elements stare from dark to light!!
    Red : 2nd index
    Blue : 1st index
    Green : 0 index
    """
    shades = [[], [], []]
    for intensity in range(70, 320, 10):
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
    def __init__(self, will_to_live:int, chance_to_fail:int, coords = None) -> None:
        """Initializing the attributes"""
        self.will_to_live = will_to_live
        self.chance_to_fail = chance_to_fail
        self.coords = coords

    def scan_for_neighbors(self):
        ...

    def megnetic_influence(self):
        ...

    def road_map(self):
        ...

    @property
    def color(self):
        """
        Student's color
        I assume that the max of each attribute can reach up to 50
        """

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
        print(self.will_to_live//2)
        return LIST_OF_COLORS[color_index][self.will_to_live//2 - 1]
