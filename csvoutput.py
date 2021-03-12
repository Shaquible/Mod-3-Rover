
import numpy
from grid import Grid
import lidar
from qset_lib import Rover
rover = Rover()
grid_width = 5
grid_height = 5
grid_res = 1
#intializes grid and sets target position in array coordinates
grid = Grid(grid_width, grid_height, grid_res, default_value=0.0)
changed = lidar.update_grid(rover.y, rover.y, rover.heading, rover.laser_distances, grid)
print(changed)
print(grid)
arr = numpy.asarray(grid)
arr.tofile('grid1.csv', sep = ',')
