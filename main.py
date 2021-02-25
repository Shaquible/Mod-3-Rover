from qset_lib import Rover
import move
import lidar
import dstar
#define node grid

def main():
    rover = Rover()
    x_target = float(input ("Target x coordinate"))
    y_target = float(input ("Target y coordinate"))
    grid_x = 10
    grid_y = 10
    grid_res = 0.5
    lidar.updategrid()
    dstar.compute()
    move.movement()

    
