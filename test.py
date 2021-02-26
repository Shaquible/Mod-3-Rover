from qset_lib import Rover
import math
import time
rover = Rover()
while round(rover.x, 1) != 1-0.4:
    rover.send_command(1,0)
    print(rover.x)
rover.send_command(0,0)
time.sleep(5)
print(rover.x)

