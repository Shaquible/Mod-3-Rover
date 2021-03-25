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
    while True:
        try:
            x_target = int(input("Please Enter your x target: "))
            y_target = int(input("Please Enter your y target: "))
        except NameError:                                                  
            print("That was not a valid input, try again ")
            continue
        else:
            break
    
    grid_width = 99
    grid_height = 99
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
    time.sleep(1)
    print changed
    csvoutput.read(grid, 'grid')
    current = dlite.start
    n_list = dlite.sense_map(7)

    #updates nodes near rover if affected by obstacles
    if changed == True:
        dlite.km += dlite.heuristics(current,dlite.start)
        current = dlite.start
        #records change in sensed map
        for n in n_list:
            if(dlite.sensed[n[0]][n[1]] != grid[n[0]][n[1]]):
                dlite.sensed[n[0]][n[1]] = grid[n[0]][n[1]]
                print dlite.sensed[n[0]][n[1]]
                dlite.update_vertex(n)
        dlite.get_shortest_path()
    path = [dlite.start] # list of path nodes for testing
    dlite.get_shortest_path()
    
    #run until goal is reached
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
        print changed 
        
        #update nodes near rover's current position if obstacles are detected
        in_sense = True
        n_list = dlite.sense_map(7)

        for n in n_list:
            if(dlite.sensed[n[0]][n[1]] != grid[n[0]][n[1]]):
                in_sense = False
        #update edge costs near the rover's position
        if changed == True or in_sense == False:
            dlite.km += dlite.heuristics(current,dlite.start)
            current = dlite.start
            
            for n in n_list:
                if(dlite.sensed[n[0]][n[1]] != grid[n[0]][n[1]]):
                    dlite.sensed[n[0]][n[1]] = grid[n[0]][n[1]]
                    dlite.update_vertex(n)
            dlite.get_shortest_path()
    
    dlite.get_shortest_path()
    csvoutput.read(path, 'path')
    end = time.time()
    time_elasped = str(end - start)
    print("Time elasped: " + time_elasped + " seconds")
    csvoutput.read(grid, 'grid')
Main()