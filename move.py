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
        if y > 0:
            heading = 90
        if y < 0:
            heading = -90
        float(heading)
        return heading
    else:
        heading = 180/math.pi * math.atan(abs(y / x))
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
def turn(targetx, targety, time_fact):
    rover = Rover()
    for i in range(3):
        #gathers target heading
        delta_x = targetx - rover.x
        delta_y = targety - rover.y
        target_head = heading(delta_x, delta_y)
        #sets perameters for each turn step
        angularv = 2
        wait = 2/3 * time_fact
        precision = 0
        if i == 1:
            angularv = 0.5
            wait = 4/3 * time_fact
            precision = 1
        if i == 2:
            angularv = 0.07
            precision = 3
            wait = 0

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
            if 0 < rover.heading < 90 and 0 > target_head > -90:
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
            print(rover.heading, target_head, i)
        #stops over steer
        rover.send_command(0,-0.001*angularv)
        rover.send_command(0,0)
        #defines time to wait between angle computations to account for oversteer
        time.sleep(wait)
    delta_x = targetx - rover.x
    delta_y = targety - rover.y
    time.sleep(4/15 * time_fact)
    return (delta_x, delta_y)


def drive(targetx, targety, dx, dy):
    rover = Rover()
    #drives in 2 steps with decreasing speed once close enough to target
    for j in range (2):
        if targetx % 1 != 0 and targety % 1 != 0:
            precision = 1
            v = 0.2
        if j == 1:
            precision = 1
            v = 0.02
            #0.01 deffinetly works
        
        if j == 0:
            precision = 0
            v = 0.75
        if targetx % 1 != 0 and targety % 1 != 0:
            precision = 1
          
        #moves rover forward and checks how close it is to the target position
        while round(rover.x, precision) != round(targetx, precision) or round(rover.y, precision) != round(targety, precision):
            rover.send_command(v, 0)
            #for debugging
            print(rover.x, rover.y, j, targetx, targety)
        rover.send_command(-0.00002, 0)

    return True


def movement(targetx, targety, time_fact):
    rover = Rover()
    Drive = False
    while Drive == False:
        dx, dy = turn(targetx, targety, time_fact)
        Drive = drive(targetx, targety, dx, dy)
    #wait to see how far any oversteer went used for testing drive should be hashed off for actual use
    #time.sleep(2)
    print(rover.x,rover.y,rover.heading)





