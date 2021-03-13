import math



# update_grid will read the lidar array and update the grid in place
# It will return True if any changes were actually made, and False otherwise
def update_grid(x, y, heading, laser_distances, grid, grid_resolution):
    made_changes = False

    for i, distance in enumerate(laser_distances):
        # angle is in radians
        if heading > 0:
            heading = 360 + heading 
            
        angle = heading * math.pi / 180.0 + math.pi * (i - 7) / 28.0
        if math.isinf(distance):
            continue

        # heading of 0 deg = +X
        # heading of 90 deg = +Y

        #gets world coordinates of the object
        world_x = distance * math.cos(angle) + x
        world_y = distance * math.sin(angle) + y

        #rounds world coordinates to grid coordinates
        grid_x = int(world_x / grid_resolution) + int(len(grid[0]) / 2)
        grid_y = int(world_y / grid_resolution) + int(len(grid) / 2)
        if grid_x == int(x / grid_resolution) + int(len(grid[0]) / 2) and grid_y == int(y / grid_resolution) + int(len(grid) / 2):
            continue

        #compares old grid to lidar data to check for changes
        old = grid[grid_x][grid_y]
        new = float('inf')
        if old != new:
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                #updates grid if there is a change
                    grid[grid_x+i][grid_y+j] = new
            made_changes = True

    return made_changes