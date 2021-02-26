from qset_lib import Rover
import move
import lidar
import dstar

def main():
    rover = Rover()
    
    x_target = float(input ("Target x coordinate"))
    y_target = float(input ("Target y coordinate"))

    grid_x = 11
    grid_y = 11

    x_0 = round(grid_x/2)
    y_0 = round(grid_y/2)

    grid_res = 0.5
    grid = [[0 for x in range(grid_x)] for y in range(grid_y)]
    
    lidar.updategrid(grid_res)
    dstar.compute(x_target, y_target)
    move.movement()

    
