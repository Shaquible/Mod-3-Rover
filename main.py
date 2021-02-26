from qset_lib import Rover
from grid import Grid
import move
import lidar
import dstar

def main():
    rover = Rover()

    x_target = float(input("Target x coordinate: "))
    y_target = float(input("Target y coordinate: "))

    grid_width = 11
    grid_height = 11
    grid_res = 0.5
    grid = Grid(grid_width, grid_height, grid_res, default_value=0.0)

    changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid)
    print(grid.array)
    
    # dstar.compute(x_target, y_target)
    # move.movement()

    
