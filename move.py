import math
import time
import lidar
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


def turn(targetx, targety, time_fact, grid, grid_res):
    rover = Rover()
    changed = False
    diff = 100
         # the amount the rover's angle needs to change by
    while abs(diff) > 0.005:
        delta_x = targetx - rover.x
        delta_y = targety - rover.y
        target_head = heading(delta_x, delta_y)

        diff = target_head - rover.heading
        diff = (diff + 180) % 360 - 180
        diff = abs(diff)

        angularv = (diff * math.pi / 180.0) * 1.5
        if angularv < 0.05:
            angularv = 0.05

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

        rover.send_command(0, angularv)
        print rover.heading, target_head
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True

    rover.send_command(0, -0.00001)
    rover.send_command(0,0)
    return changed
    
#turns in 3 steps each of decreasing speed and increasing precision
def turn_old(targetx, targety, time_fact):
    rover = Rover()
    for i in range(4):
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
            angularv = 0.2
            precision = 3
            wait = 0
        if i == 3:
            angularv = 0.1
            precisioin = 3

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
            print "heading: ", rover.heading, ", target: ", target_head, ", turn step: ", i
        #stops over steer
        rover.send_command(0,-0.001*angularv)
        rover.send_command(0,0)
        #defines time to wait between angle computations to account for oversteer
        time.sleep(wait)
    delta_x = targetx - rover.x
    delta_y = targety - rover.y
    time.sleep(4/15 * time_fact)
    return (delta_x, delta_y)


def drive(targetx, targety, grid, grid_res):
    rover = Rover()
    changed = False
    #drives in 2 steps with decreasing speed once close enough to target
    
    for j in range (2):
        if targetx % 1 != 0 and targety % 1 != 0:
            precision = 1
            v = 0.2
        if j == 1:
            precision = 1
            v = 0.01
            #0.01 deffinetly works
        
        if j == 0:
            precision = 0
            v = 0.75
        if targetx % 1 != 0 and targety % 1 != 0:
            precision = 1
          
        #moves rover forward and checks how close it is to the target position
        while round(rover.x, precision) != round(targetx, precision) or round(rover.y, precision) != round(targety, precision):
            dx = targetx - rover.x
            dy = targety - rover.y
            target_head = heading(dx,dy)
            diff = target_head - rover.heading
            diff = (diff + 180) % 360 - 180
            diff = abs(diff)
            #if diff > 2:
                #return False  
            rover.send_command(v, 0)
            #for debugging
            print "driving with j=", j, ": ", (rover.x, rover.y), (targetx, targety)
            just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
            if just_changed:
                changed = True
        rover.send_command(-0.00002, 0)

    return True, changed


def movement(targetx, targety, time_fact, grid, grid_res):
    rover = Rover()
    changed = False
    Drive = False
    while Drive == False:
        change1 = turn(targetx, targety, time_fact, grid, grid_res)
        Drive, change2 = drive(targetx, targety, grid, grid_res)
        if change1 or change2:
            changed = True
    #wait to see how far any oversteer went used for testing drive should be hashed off for actual use
    #time.sleep(2)
    print rover.x,rover.y,rover.heading
    return changed





