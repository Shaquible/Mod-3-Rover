from qset_lib import Rover
import move
import math
import lidar
from dstar import DStar
import csvoutput
import time


def Main():
    start = time.time()
    rover = Rover()
    #use the gazebo real time factor of your system under a standard gazebo load
    time_fact = 0.75
    rover.send_command(0,0)
    time.sleep(2/15 * time_fact)
    #user adjustable perameters
    x_target = 8
    y_target = 0
    
    grid_width = 31
    grid_height = 31
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

    rover.send_command(0, 50)
    time.sleep(2/3 * time_fact)
    changed = False

    # this will do a full 360 and scan the area around the rover
    while rover.heading >= 0:
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True
        rover.send_command(0, 1)
        print rover.heading
    while rover.heading < 0:
        just_changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if just_changed:
            changed = True
        rover.send_command(0, 1)
        print rover.heading
    
    rover.send_command(0, -0.001)
    rover.send_command(0, 0)
    time.sleep(0.25)
    print changed
    csvoutput.read(grid)
    current = dlite.start
    sensed = dlite.sensed 
    n_list = dlite.sense_map(7)

    #ignore this, mainly for testing
    if changed == True:
        dlite.km += dlite.heuristics(current,dlite.start)
        current = dlite.start
        for n in n_list:
            if(dlite.sensed[n[0]][n[1]] != grid[n[0]][n[1]]):
                dlite.sensed[n[0]][n[1]] = grid[n[0]][n[1]]
                print dlite.sensed[n[0]][n[1]]
                dlite.update_vertex(n)
        dlite.get_shortest_path()
    #dlite.update_vertex(current)
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
        
        changed1 = move.movement(x,y, time_fact, grid, grid_res)
        path.append(dlite.start) #add to path
                #call update_grid
        changed2 = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid, grid_res)
        if changed1 or changed2:
            changed = True
        #csvoutput.read(grid)
        sensed.append(dlite.sensed)
        #if there was a change in graph, set current = self.start
        print changed 
        n_list = dlite.sense_map(7)

        #needs to also check whether a node in sensed doesnt match grid OR if changed
        #how to do that without loop?
        if changed == True:
            dlite.km += dlite.heuristics(current,dlite.start)
            current = dlite.start
            
            for n in n_list:
                if(dlite.sensed[n[0]][n[1]] != grid[n[0]][n[1]]):
                    dlite.sensed[n[0]][n[1]] = grid[n[0]][n[1]]
                    dlite.update_vertex(n)
            dlite.get_shortest_path()
    #dlite.update_vertex(current)
    dlite.get_shortest_path()
        #print path
    end = time.time()
    time_elasped = str(end - start)
    print("Time elasped: " + time_elasped)
    csvoutput.read(grid)
Main()