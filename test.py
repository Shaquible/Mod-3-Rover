import math
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
    

head = heading(-9,0)
print(head)