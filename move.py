import math
import time
from qset_lib import Rover
# will get next node in sequence from d*
#use current position and target position to get neccacary heading
#check current position against target to reach that position
#change heading
#change target to actuall target from d*
def movement(targetx, targety):
    rover = Rover()
    delta_x = targetx - rover.x
    delta_y = targety - rover.y
    if delta_x == 0:
        if delta_y > 0:
            target_head = 90
        if delta_y < 0:
            target_head = 90
    if delta_x != 0:
        target_head = 180/math.pi * math.atan(delta_y / delta_x)
        #need to convert from 0 to 360 to the +/- format of rover
    angularv = 0.6
    #this is not going to work wtih +/-
    if rover.heading > target_head:
        angularv = -1 * angularv

    while round(rover.heading, 1) != round(target_head, 1):
        rover.send_command(0, angularv)
        print(rover.heading)

    rover.send_command(0,-0.0001)
    rover.send_command(0,0)
    time.sleep(2)
    #want to turn twice to readjust
    
    rover.send_command(0,-0.1 * angularv)
    while round(rover.x, 1) != targetx && round(rover.y, 1) != targety:
        rover.send_command(0.5,0)
        print(rover.x, rover.y)
    rover.send_command(-0.1,0)

    time.sleep(2)
    print(rover.x,rover.y,rover.heading)





