from qset_lib import Rover
import lidar
import math
from grid import Grid
from lidar import update_grid
import heapq


rover=Rover()

#dk if we need a class for it but nodes list will be a 1d list with (x,y) pairs of same quantity as grid
class Node:
    pass
    def __init__(self, world_grid):
        self.x = x
        self.y = y

def __init__(self,start,goal,world_grid): #initialize starting values
    pass
    self.start = start
    self.position = start
    self.goal = goal
    self.queue = [] #dk about this for now
    self.km = 0
    self.world_grid = world_grid #world grid from main
    self.nodes = [] #create list of nodes from grid?
    self.open_set = PriorityQueue(0, 0, start) #initialize priority queue with start node only
    self.open_set_hash = {start} #copy of queue with node only (to keep track of whats inside the queue)
    self.came_from = {} #list that stores all previous nodes in final path
    self.rhs = [[float('inf') for x in range(len(self.world_grid[0]))] for y in range(len(self.world_grid))] #2d array same as world grid but with infinity values
    self.g = self.rhs.copy()
    self.rhs[self.goal[0]][self.goal[1]] = 0
    

def get_shortest_path(self):
    pass
    #loop while queue is not empty and lowest key is less than start key or rhs does not equal g for start
    while not open_set.empty and self.g[self.start[0]][self.start[1]] < self.rhs[self.start[0]][self.start[1]]:
        u = open_set.get()[2] #get node lowest in queue
        key_old = open_set.get()[0] #get lowest key
        key_new = computeKey(u) #get key of u
        s_list = neighbours(u) #neighbouring nodes

        if(key_old < key_new): #if lowest key is less than key of u
            open_set.put(key_new) #add new key to queue

        elif(self.g[u[0]][u[1]] > self.rhs[u[0]][u[1]]: #if overconsistent
            self.g[u[0]][u[1]] = self.rhs[u[0]][u[1]] #set g and rhs equal
            open_set.remove(u) #and remove u from queue
          
            #loop thru all nodes s in neighbours list
            for s in s_list:
                self.update_vertex(s) #call update_vertex for each s
        #when locally inconsistent        
        else:
            self.g[u[0]][u[1]] = float('inf') #g is inf
            
            s_list.append(u) #add u to neighbour list
            for s in s_list: #loop thru neighbours and call update_vertex
                self.update_vertex(s)


def computeKey(self,s):
    pass
    key = [0,0]
    key[0] = min(self.g[s[0]][s[1]],self.rhs[s[0]][s[1]]) + heuristics(self.start,s)+self.km
    key[1] = min(self.g[s[0]][s[1]],self.rhs[s[0]][s[1]])
    return key


def update_change(self): 
    pass
    changed = lidar.update_grid(rover.x, rover.y, rover.heading, rover.laser_distances, grid)
    if changed:
        self.km += heuristics(self.goal)

#function to check for change in edge cost
# if function return true, change K_m to be h(s) from the start to the goal (looped).

def heuristics(self,s): #distance from current node to start.
    pass
    x1,y1 = self.start
    x2,y2 = s
    node_x = abs(x1-x2)
    node_y = abs(y1-y2)
    node_final = math.sqrt((node_x**2)+(node_y**2))
    
    return node_final


#cost of movement from u to s
def cost(self,u,s):
    pass
    x1, y1 = u
    x2,y2 = s
    #note: this is temporary we prob have to check for obstacles another way
    #if the value at node u or s is inf (i.e obstacle is detected), cost is inf 
    if(self.world_grid[x1][y1] == float('inf') or self.world_grid[x2][y2] == float('inf')):
        return float('inf')
    #if no obstacles, cost will be one
    else:
        return 1

#look for successors or predecessors of node u
def neighbours(self,u):
    pass
    x,y = u
    #list of all possible 8 neighbouring nodes
    nodes_near = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
    filtered = []
    #check if said neighbouring node exists in original node list
    for s in nodes_near:
        if s[0] >= 0 and s[0] < len(self.nodes) and s[1] >= 0 and s[1] < len(self.nodes[0]):
            filtered.append(s) #if it does, add to a new list with only existing neighbours
    return filtered #return the new list


def update_vertex(self,u): #compare the g and rhs values for a node, check if node is on priority queue.
    pass
    #if we are not on the goal node
    if u != self.goal:
        #get the neighbouring nodes of u
        nodes_near = self.neighbours(u)
        lowest_cost = float('inf')

        #loop through all nodes s in the list of neighbours
        for s in nodes_near:
            #if the movement cost from u to s added to the g(s) is lower than predicted minimum cost
            if self.cost(u,s) + self.g[s[0]][s[1]] < lowest_cost:
                
                #update lowest cost to be that sum
                lowest_cost = self.cost(u,s) + self.g[s[0]][s[1]]
        
        #once the final lowest lookahead g(u) is found, update rhs 
        self.rhs[u[0]][u[1]]=lowest_cost
    self.open_set_hash # -> list of all nodes in queue
    if u in open_set_hash:
        open_set.remove(u)
        open_set_hash.remove(u)

    if self.g[u[0]][u[1]] != self.rhs[u[0]][u[1]]:
            open_set.put(u)
            open_set_hash.put(u)
    #check if u is in queue and if it is, remove it from queue
    #then check if g(u) does NOT equal rhs(u) and add u to queue

def plan_path(self):
    current = self.start
    self.get_shortest_path()
    while self.start != self.goal:
        if(self.g[self.start[0]][self.start[1]]) == float('inf'):
            #no path
        
        #change start to neighbouring node with lowest cost
        #if there was a change in graph, set current = self.start
        #call updatevertex and compute path functions
