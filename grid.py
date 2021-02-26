
class Grid:

    def __init__(self, width, height, resolution, default_value=0):
        assert width % 2 == 1, "width should be odd"
        assert height % 2 == 1, "height should be odd"
        self.array = [[default_value for x in range(width)] for y in range(height)]
        self.width = width
        self.height = height
        self.resolution = resolution

    def get_coordinate(self, x, y):
        return self.array[x + int(self.width / 2)][y + int(self.height / 2)]

    def set_coordinate(self, x, y, val):
        self.array[x + int(self.width / 2)][y + int(self.height / 2)] = val

