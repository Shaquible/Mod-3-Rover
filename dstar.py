from qset_lib import Rover
import lidar
import math
from Queue import PriorityQueue
from grid import Grid
from lidar import update_grid
import heapq


rover=Rover()
q = PriorityQueue()
grid_edge_cost = 1

def __init__(self,start,goal): #initialize starting values
    pass
    self.start = start
    self.postition = start
    self.goal = goal
    self.g = float('inf')
    self.km = 0
    self.rhs = float('inf') #0 for the goal node

def computeKey(s, start_node):
    pass
    key = [0,0]
    key[0] = min(g[s],rhs[s]) + h(self.start,s)+km
    key[1] = min(g[s],rhs[s])
    return key

def update_change(x, y): #find shortest path
    pass

#function to check for change in edge cost
# if function return true, change K_m to be h(s) from the start to the goal (looped).

def heuristics(start, s2): #distance from current node to start.
    pass
    x1, y1 = start
    x2, y2 = s2
    node_x = abs(x1 - x2)
    node_y = abs(y1 - y2)
    node_final = math.sqrt((node_x**2)+(node_y**2))
    #must be 0 for start node
    return node_final
    
def get_g(s): # gets g value (distance from goal to node) for node s 
    pass


def get_rhs(s): #gets rhs value for node s (same process as g value).
    pass

def pre(s): #finds predecessor node for current node s.
    pass

def suc(s): # find successor node for currne tnode s.
    pass

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

