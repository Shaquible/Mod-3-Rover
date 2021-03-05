from qset_lib import Rover
from grid import Grid
import move
import lidar
import dstar

def Main():
    rover = Rover()

    x_target = 4
    y_target = 5

    grid_width = 11
    grid_height = 11
    grid_res = 0.5
    grid = Grid(grid_width, grid_height, grid_res, default_value=0.0)

    changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid)
    if changed == True:
        dstar.compute(x_target, y_target)
    #update d* queue
    #get next target from d*
    node_x = 30.25
    node_y = -20
    move.movement(node_x, node_y)

    
main()