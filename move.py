import math
import time
from qset_lib import Rover
# will get next node in sequence from d*
#use current position and target position to get neccacary heading
#check current position against target to reach that position
#change heading
#change target to actuall target from d*
def heading(x, y)
    if x == 0:
    heading = 0
    else:
        heading = 180/math.pi * math.atan(abs(y / x))
    if y <= 0 and x >= 0:
        heading = -1 * heading
    if y <= 0 and x <= 0:
        heading = -180 - -1 * heading
    if y >= 0 and x <= 0:
        heading = 180 - heading    
    return heading

def movement(targetx, targety):
    rover = Rover()
    for i in range 2:
        delta_x = targetx - rover.x
        delta_y = targety - rover.y
        target_head = heading(delta_x, delta_y)
        angularv = 0.6
        if rover.heading >= 0 and target_head >= 0:
            if rover.heading > target_head:
                angularv = -1 * angularv
        if rover.heading < 0 and target_head < 0:
            if rover.heading > target_head:
                angularv = -1 * angularv
        while round(rover.heading, 1) != round(target_head, 1):
            rover.send_command(0, angularv)
            print(rover.heading)

        rover.send_command(0,-0.001*angularv)
        rover.send_command(0,0)
    
    
    rover.send_command(0,-0.1 * angularv)
    while round(rover.x, 1) != targetx and round(rover.y, 1) != targety:
        rover.send_command(0.5,0)
        print(rover.x, rover.y)
    rover.send_command(-0.001,0)

    time.sleep(2)
    print(rover.x,rover.y,rover.heading)





