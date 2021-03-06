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
        float(heading)
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
    return heading
#turns in 3 steps each of decreasing speed and increasing precision
def turn(targetx, targety):
    rover = Rover()
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
            cw = 0
            if rover.heading > 0 and target_head > 0:
                if rover.heading > target_head:
                    angularv = -1 * abs(angularv)
                    cw = 1
            if rover.heading < 0 and target_head < 0:
                if abs(rover.heading) < abs(target_head):
                    cw = 1
                    angularv = -1 * abs(angularv)
            if rover.heading < -90 and target_head > 90:
                angularv = -1 * abs(angularv)
                cw = 1
            if cw == 0:
                angularv = abs(angularv)

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
    delta_x = targetx - rover.x
    delta_y = targety - rover.y
    return (delta_x, delta_y)

def drive(targetx, targety, dx, dy):
    rover = Rover()
    initial_x = rover.x
    initial_y = rover.y
    #drives in 2 steps with decreasing speed once close enough to target
    for i in range (2):
        max_x = abs(dx) + 0.3
        max_y = abs(dy) + 0.3
        precision = 2
        v = 0.01
        wait = 0
        if i == 0:
            precision = 0
            v = 0.75
            wait = 0.5
        #moves rover forward and checks how close it is to the target position
        while round(rover.x, precision) != targetx or round(rover.y, precision) != targety:
            rover.send_command(v, 0)
            #for debugging
            print(rover.x, rover.y, i)
            #this may not work
            traveledx = abs(rover.x - initial_x)
            traveledy = abs(rover.y - initial_y)
            if traveledx > max_x or traveledy > max_y:
                rover.send_command(-0.02, 0)
                return False
        
        rover.send_command(-0.02, 0)
        time.sleep(wait)

    return True

def movement(targetx, targety):
    rover = Rover()
    Drive = False
    while Drive == False:
        dx, dy = turn(targetx, targety)
        Drive = drive(targetx, targety, dx, dy)
    #wait to see how far any oversteer went used for testing drive should be hashed off for actual use
    time.sleep(2)
    print(rover.x,rover.y,rover.heading)





