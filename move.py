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

#turns the rover to a target heading that will lead to the next node
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
        #sets velocity to a function of difference in heading and has a min velocity
        angularv = (diff * math.pi / 180.0) * 1.5
        if angularv < 0.1:
            angularv = 0.1
        #cumputes whether to turn clockwise or counter clockwise
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
        print "Turning from: ", (rover.heading), "to", (target_head)
        #updates grid
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True

    rover.send_command(0, -0.00001)
    rover.send_command(0,0)
    return changed
    
#drives the rover to a target node
def drive(targetx, targety, grid, grid_res):
    rover = Rover()
    sucsess = False
    changed = False
    diff = 1000
    while diff > 0.05:
        #computed distance left to drive
        y_diff = targety - rover.y
        x_diff = targetx - rover.x
        diff = math.sqrt(x_diff ** 2 + y_diff ** 2)
        #computes weather the rover has gone too far and will not reach the node
        if round(diff, 5) > 1.5 * grid_res:
            sucsess = False
            return sucsess, changed
        
        #speed is a fn of the distance
        speed = diff * 0.75
        #sets max speed
        if speed > 1.5:
            speed = 1.5
        rover.send_command(speed, 0)
        print "Driving from: ", (rover.x, rover.y), "to", (targetx, targety)
        #updates grid as its driving
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True
    rover.send_command(-0.00001,0)
    rover.send_command(0,0)
    sucsess = True
    return sucsess, changed
#moves the rover to the rarget by turning then driving and checks the lidar array during the drive process
def movement(targetx, targety, time_fact, grid, grid_res):
    rover = Rover()
    changed = False
    Drive = False
    while Drive == False:
        change1 = turn(targetx, targety, time_fact, grid, grid_res)
        Drive, change2 = drive(targetx, targety, grid, grid_res)
        if change1 or change2:
            changed = True
    print rover.x,rover.y,rover.heading
    return changed





