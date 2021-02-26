
# A Grid is a 2D array which can be accessed using negative coordinates.
# A grid keeps its width, height, and resolution
class Grid:

    # Initializes the grid with a width, height, resolution, and an optional default value
    def __init__(self, width, height, resolution, default_value=0):
        assert width % 2 == 1, "width should be odd"
        assert height % 2 == 1, "height should be odd"
        self.array = [[default_value for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.resolution = resolution

    # Gets a coordinate. It will convert grid x and y to an array x and y, which means
    # negative coordinates can be used.
    #
    # e.g. assume the grid's width and height are 7 and 7
    # grid.get_coordinate(-1, 3) == grid.array[2][6]
    def get_coordinate(self, x, y):
        return self.array[x + int(self.width / 2)][y + int(self.height / 2)]

    # Sets a coordinate to val. It will convert grid x and y to an array x and y, which means
    # negative coordinates can be used.
    #
    # e.g. assume the grid's width and height are 7 and 7
    # grid.set_coordinate(-1, 3, 0)
    #    is equivalent to:
    # grid.array[2][6] = 0
    #
    def set_coordinate(self, x, y, val):
        self.array[x + int(self.width / 2)][y + int(self.height / 2)] = val

