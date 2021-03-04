import math
x = -2
y = -1
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
print(heading)