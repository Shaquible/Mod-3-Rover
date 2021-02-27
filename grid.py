
#
# COORDINATE SYSTEMS:
#
# World coordinates are in meters, and are in the range (-inf, inf)
# 
# Grid coordinates are integers, and are in the range [-width/2, width/2] or [-height/2, height/2],
# for x and y, respectively. They are resolution-dependent and can be negative.
#
# Array coordinates are integers, and are in the range [0, width) or [0, height), for x and y,
# respectively. Array coordinates are handled in this class automatically, and shouldn't really
# be used. Use grid coordinates and call this class's get_coordinate and set_coordinate methods.
#


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

