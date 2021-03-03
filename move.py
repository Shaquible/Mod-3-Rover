import math
# will get next node in sequence from d*
#use current position and target position to get neccacary heading
#check current position against target to reach that position
def movement(targetx, targety):
#change heading
#change target to actuall target from d*
    delta_x = targetx - rover.x
    delta_y = targety - rover.x
    target_head = 180/math.pi * math.atan(delta_y / delta_x)
    angularv = 0.25
    if rover.heading > target_head:
        angularv = -angularv

    while round(rover.heading, 1) != round(target_head, 1):
        rover.send_command(0, angularv)
        print(rover.heading)

    rover.send_command(0,-angularv)
    time.sleep(0.5)
    while round(rover.x, 1) < targetx and round(rover.y, 1) < targety:
        rover.send_command(0.5,0)
        print(rover.x, rover.y)
    rover.send_command(-0.5,0)

    time.sleep(2)
    print(rover.x,rover.y)




