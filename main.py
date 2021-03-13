from qset_lib import Rover
import move
import math
import lidar
from dstar import DStar
import csvoutput
import time


def Main():
    rover = Rover()
    rover.send_command(0,0)
    time.sleep(0.1)
    #user adjustable perameters
    x_target = 4
    y_target = 4
    
    grid_width = 51
    grid_height = 51
    grid_res = 1
    #intializes grid and sets target position in array coordinates
    grid = [[0.0 for x in range(grid_width)] for y in range(grid_height)]
    startx = int((rover.x) / grid_res)
    starty = int((rover.y) / grid_res)
    x_target = int((x_target) / grid_res)
    y_target = int((y_target) / grid_res)
    start_node = startx+ int(grid_width/2),starty+ int(grid_height/2)
    goal_node = x_target+ int(grid_width/2),y_target+int(grid_height/2)
    dlite = DStar(start_node, goal_node, grid)

    rover.send_command(0, 1)
    time.sleep(0.01)
    changed = False

    # this will do a full 360 and scan the area around the rover
    while round(rover.heading, 1) != 0.0:
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True
        rover.send_command(0, 1)
    
    rover.send_command(0, -0.001)
    rover.send_command(0, 0)

    current = dlite.start
    sensed = dlite.sensed 
    n_list = dlite.sense_map(3)
    print(changed)

    #ignore this, mainly for testing
    """if changed == True:
        dlite.km += dlite.computeKeyheuristics(current,dlite.start)
        current = dlite.start
        for n in n_list:
            if(dlite.sensed[n[0]][n[1]] != dlite.world_grid[n[0]][n[1]]):
                dlite.sensed[n[0]][n[1]] = dlite.world_grid[n[0]][n[1]]
                dlite.update_vertex(n)
        dlite.get_shortest_path()"""

    path = [dlite.start] # list of path nodes for testing
    dlite.get_shortest_path()
    
    while dlite.start != dlite.goal:
        
        #change start to neighbouring node with lowest cost
        s_list = dlite.neighbours(dlite.start)
        min_neighbour = float('inf')
        for s in s_list:
            if dlite.cost(dlite.start,s) + dlite.g[s[0]][s[1]] < min_neighbour:
                min_neighbour = dlite.cost(dlite.start,s) + dlite.g[s[0]][s[1]]
                min_node = s

        dlite.start = min_node
        
        #move the rover to x and y
        #get x and y coordinates from node
        x = (dlite.start[0] - int(len(dlite.world_grid[0])/2)) * grid_res
        y = (dlite.start[1] - int(len(dlite.world_grid)/2)) * grid_res
        
        move.movement(x,y)
        path.append(dlite.start) #add to path
                #call update_grid
        changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        #csvoutput.read(grid)
        sensed.append(dlite.sensed)
        #if there was a change in graph, set current = self.start
        print(changed) 
        
        #don't think this part works properly
        if changed == True:
            dlite.km += dlite.heuristics(current,dlite.start)
            current = dlite.start
            for n in n_list:
                if(dlite.sensed[n[0]][n[1]] != dlite.world_grid[n[0]][n[1]]):
                    dlite.sensed[n[0]][n[1]] = dlite.world_grid[n[0]][n[1]]
                    dlite.update_vertex(n)
            dlite.get_shortest_path()
        
        dlite.get_shortest_path()
        print(path)
Main()