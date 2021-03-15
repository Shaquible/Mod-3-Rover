from qset_lib import Rover
import csvoutput
import lidar
import time
rover = Rover()
grid_width = 11
grid_height = 11
grid_res = 0.5
rover.send_command(0,0)
time.sleep(0.1)
arr = rover.laser_distances
print arr
#intializes grid and sets target position in array coordinates
grid = [[0.0 for x in range(grid_width)] for y in range(grid_height)]
changes = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
print changes
csvoutput.read(grid)
