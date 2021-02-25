from qset_lib import Rover
import move
import lidar
import dstar

def main():
    rover = Rover()
    x_target = float(input ("Target x coordinate"))
    y_target = float(input ("Target y coordinate"))

    lidar.updategrid()
    dstar.compute()
    move.movement()
    
