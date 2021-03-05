from qset_lib import Rover
import lidar
import math
from grid import Grid
from lidar import update_grid
import heapq


rover=Rover()
q = PriorityQueue()
grid_edge_cost = 1

def __init__(self,start,goal,grid): #initialize starting values
    pass
    self.start = start
    self.position = start
    self.goal = goal
    self.g = float('inf')
    self.queue = []
    self.km = 0
    self.grid = grid #world grid 
    self.nodes = [] #create list of nodes from grid?
    self.rhs = float('inf') #0 for the goal node

def computeKey(s, start_node):
    pass
    key = [0,0]
    key[0] = min(g[s],rhs[s]) + heuristics(self.start,s)+km
    key[1] = min(g[s],rhs[s])
    return key

def update_change(x, y): #find shortest path
    pass

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
    
def get_g(s): # gets g value (distance from goal to node) for node s 
    pass


def get_rhs(s): #gets rhs value for node s (same process as g value).
    pass

#cost of movement from u to s
def cost(self,u,s):
    pass
    x1, y1 = u
    x2,y2 = s
    #note: this is temporary we prob have to check for obstacles another way
    #if the value at node u or s is inf (i.e obstacle is detected), cost is inf 
    if(self.grid[x1][y1] == float('inf') or grid[x2][y2] == float('inf')):
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


def update_vertex(s): #compare the g and rhs values for a node, check if node is on priority queue.
    pass
    if g(s) != rhs(s):
        if g(s) > rhs(s):
            pass
            #set values equal to eachother
            #update all predecessors of s.
            #over consistent
        if g(s) < rhs(s):
            pass
            #set g(s) equal to inf
            #update all predecessors of s and s itself.
            #under consistent

def get_shortest_path():
    pass

