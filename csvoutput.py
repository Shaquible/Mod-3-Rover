import csv

def csv(grid):
    filename = gird1.csv
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writter(csvfile)
        csvwriter.writerows(grid)
