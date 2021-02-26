import math
from grid import Grid


# update_grid will read the lidar array and update the grid in place
# It will return True if any changes were actually made, and False otherwise
def update_grid(x, y, heading, laser_distances, grid):
    made_changes = False

    for i, distance in enumerate(laser_distances):
        # angle is in radians
        angle = heading * math.pi / 180.0 + math.pi * (i - 7) / 28.0

        # heading of 0 deg = +X
        # heading of 90 deg = +Y
        world_x = distance * math.cos(angle) + x
        world_y = distance * math.sin(angle) + y
        grid_x = int(round(world_x * grid.resolution))
        grid_y = int(round(world_y * grid.resolution))
        grid.set_coordinate(grid_x, grid_y, float('inf'))

    return made_changes

grid = Grid(99, 99, 0.5, default_value=0.0)
update_grid(0, 0, 0, range(15), grid)
print(grid.array)