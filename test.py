from qset_lib import Rover
import math
import time
rover = Rover()
target = 10
while round(rover.x, 1) < target -0.1:
    rover.send_command(0.415,0)
    print(rover.x)
rover.send_command(0,0)
time.sleep(3)
print(rover.x)

#should use threading and wait to delay send commands but constantly check position to hault
