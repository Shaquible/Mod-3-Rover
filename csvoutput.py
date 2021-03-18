import csv
def read(grid, name):
    filename = name + '.csv'
    with open( filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        out = grid
        csvwriter.writerows(out)