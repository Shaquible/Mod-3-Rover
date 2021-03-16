from qset_lib import Rover
import csvoutput
import lidar
import time
import move
rover = Rover()
grid_width = 99
grid_height = 99
grid_res = 1
#intializes grid and sets target position in array coordinates
grid = [[0.0 for x in range(grid_width)] for y in range(grid_height)]

x = 1
y = -1
move.movement(x,y, 0.75, grid,grid_res)
rover.send_command(0,0)
time.sleep(2)
print(rover.x, rover.y)
