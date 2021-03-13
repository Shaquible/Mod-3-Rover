from qset_lib import Rover
import csvoutput
import lidar

grid_width = 51
grid_height = 51
grid_res = 0.5
#intializes grid and sets target position in array coordinates
grid = [[0.0 for x in range(grid_width)] for y in range(grid_height)]
changes = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
print(changes)
csvoutput.read(grid, grid_height)
