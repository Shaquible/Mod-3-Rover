from qset_lib import Rover
from grid import Grid
import move
import lidar
from dstar import DStar

def Main():
    rover = Rover()

    x_target = 4
    y_target = 5

    grid_width = 11
    grid_height = 11
    grid_res = 0.5
    grid = Grid(grid_width, grid_height, grid_res, default_value=0.0)

    start_node = (1,1)
    goal_node = (2,2)

    dlite = DStar(start_node,goal_node,grid)


    current = dlite.start
    dlite.get_shortest_path()
    path = [dlite.start] # list of path nodes for testing
    
    while dlite.start != dlite.goal:
            
        #change start to neighbouring node with lowest cost
        s_list = dlite.neighbours(dlite.start)
        min_neighbour = float('inf')
        for s in s_list:
            if dlite.cost(dlite.start,s) + dlite.g[s[0]][s[1]] < min_neighbour:
                min_neighbour = dlite.cost(dlite.start,s) + dlite.g[s[0]][s[1]]
                min_node = s

        dlite.start = min_node.copy()
        path.append(dlite.start) #add to path
        #get x and y coordinates from node
        x = dlite.start[0] - int(len(dlite.world_grid[0])/2)
        y = dlite.start[1] - int(len(dlite.world_grid)/2)
        #move the rover to x and y
        move.movement(x,y)

        #call update_grid
        changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid)
        
        #if there was a change in graph, set current = self.start
        if changed:
            dlite.km += dlite.heuristics(current,dlite.start)
            current = dlite.start
            #go thru all nodes with changes then update vertex for each?
            dlite.update_vertex(current)
            dlite.get_shortest_path()
    
Main()