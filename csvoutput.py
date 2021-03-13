import csv
from grid import Grid
def read(grid, grid_height):
    with open('grid.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        out = grid.array
        csvwriter.writerows(out)