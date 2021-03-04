import math
import time
from qset_lib import Rover
# will get next node in sequence from d*
#use current position and target position to get neccacary heading
#check current position against target to reach that position

#computes the heading to get to the target from current based on change in x and y
#changes angle from 0-360 to the +/-180 of the rover heading
def heading(x, y):
    if x == 0:
        heading = 0
        return heading
    else:
        heading = 180/math.pi * math.atan(abs(y / x))
        print (heading)
    if y <= 0 and x >= 0:
        heading = -1 * heading
        return heading
    if y <= 0 and x <= 0:
        heading = -180 + 1 * heading
        return heading
    if y >= 0 and x <= 0:
        heading = 180 - heading
        return heading

def movement(targetx, targety):
    rover = Rover()
    #turns in 3 steps each of decreasing speed and increasing precision
    for i in range (3):
        delta_x = targetx - rover.x
        delta_y = targety - rover.y
        target_head = heading(delta_x, delta_y)
        angularv = 2
        wait = 0.5
        precision = 0
        if i == 1:
            angularv = 0.2
            wait = 1
            precision = 1
        if i == 2:
            angularv = 0.05
            precision = 3
        
        while round(rover.heading, precision) != round(target_head, precision):
            #tells rover which way to turn
            if rover.heading >= 0 and target_head >= 0:
                if rover.heading > target_head:
                    angularv = -1 * angularv
            if rover.heading < 0 and target_head < 0:
                if rover.heading > target_head:
                    angularv = -1 * angularv
            if rover.heading < -90 and target_head > 90:
                angularv = -1 * angularv
            #turns rover
            rover.send_command(0, angularv)
            #used for debugging
            print(rover.heading, i, target_head)
        #stops over steer
        rover.send_command(0,-0.001*angularv)
        rover.send_command(0,0)
        #defines time to wait between angle computations to account for oversteer
        time.sleep(wait)
        #might not need this line
    rover.send_command(0,-0.1 * angularv)
    #drives in 2 steps with decreasing speed once close enough to target
    for i in range (2):
        precision = 2
        wait = 0
        v = 0.01
        if i == 0:
            precision = 0
            wait = 1
            v = 0.75
        #moves rover forward and checks how close it is to the target position
        while round(rover.x, precision) != targetx or round(rover.y, precision) != targety:
            rover.send_command(v,0)
            #for debugging
            print(rover.x, rover.y)
        rover.send_command(-0.02,0)
        #wait time to account for oversteer
        time.sleep(wait)
    #wait to see how far any oversteer went
    time.sleep(2)
    print(rover.x,rover.y,rover.heading)





