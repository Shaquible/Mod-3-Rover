import csv
def read(grid):
    with open('grid.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        out = grid
        csvwriter.writerows(out)