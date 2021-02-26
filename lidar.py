import math

# update_grid will read the lidar array and update the grid in place
# It will return True if any changes were actually made, and False otherwise
def update_grid(x, y, heading, lidar_array, grid):
    made_changes = False

    for i, laser in enumerate(lidar_array):
        angle = heading + math.pi * ((i - 7) / 28.0)
        print(i, angle)

    return made_changes

update_grid(0, 0, 0, range(15), 0)
