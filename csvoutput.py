import pandas
import numpy
from grid import Grid
import lidar
from qset_lib import Rover
rover = Rover()
changed = lidar.update_grid(rover.y, rover.y, rover.heading, rover.laser_distances, grid)
print(changed)
grid = numpy.asarray(a, dtype=None, order=None, *, like=None)
DF = pandas.DataFrame(grid)
DF.to_csv("grid1.csv")