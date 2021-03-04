from qset_lib import Rover
import math
from Queue import PriorityQueue
from grid import Grid
from lidar import update_grid
import heapq


rover=Rover()
q = PriorityQueue()
grid_edge_cost = 1

# figure out how the grid works and how to implement it.

def __init__(self,start,goal): #initialize starting values
    pass
    self.start = start
    self.postition = start
    self.goal = goal
    self.g = float('inf')
    self.km = 0
    self.rhs = float('inf') #0 for the goal node

def computeKey(self, s, start_node):
    pass
    self.key = [0,0]
    self.key[0] = min(g[s],rhs[s]) + h(self.start,s)+km
    self.key[1] = min(g[s],rhs[s])
    return key

def update_change(self, x, y): #find shortest path
    pass

#function to check for change in edge cost
# if function return true, change K_m to be h(s) from the start to the goal (looped).

def heuristics(self, start, s2): #distance from current node to start.
    pass
    x1, y1 = start
    x2, y2 = s2
    self.node_x = abs(x1 - x2)
    self.node_y = abs(y1 - y2)
    self.node_final = math.sqrt((node_x**2)+(node_y**2))
    #must be 0 for start node
    return node_final
    
def get_g(self, s): # gets g value (distance from goal to node) for node s 
    pass


def get_rhs(self, s): #gets rhs value for node s (same process as g value).
    pass

def pre(self, s): #finds predecessor node for current node s.
    pass

def suc(self, s): # find successor node for currnet node s.
    pass

def update_vertex(self, s): #compare the g and rhs values for a node, check if node is on priority queue.
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

def get_shortest_path(self):
    pass

def update_neightbours(self ,s):
    pass
    self.neighbours = []
    self.coordinate = grid.get_coordinate(s)
    self.max_x = grid.width
    self.max_y = grid.height
    row , col = coordinate

    if row > 0: #check to see if there is a row of nodes below the current node
        self.neighbours.append(coordinate[row][col-1]) # adds bottom node to neighbour list
        self.neighbours.append(coordinate[row-1][col-1]) # adds bottom left node to neighbour list
        self.neighbours.append(coordinate[row+1][col-1]) # adds bottom right node to neighbour list

    if row < max_x: #check to see if there is a row of nodes above the current node
        self.neighbours.append(coordinate[row][col+1]) # adds top node to neighbour list
        self.neighbours.append(coordinate[row-1][col+1]) # adds top left node to neighbour list
        self.neighbours.append(coordinate[row+1][col+1]) # adds top right node to neighbour list
    
    if col > 0: #check to see if there is a colunm of nodes to the left of the current node
        self.neighbours.append(coordinate[row+1][col]) # add right node to neighbour list
        self.neighbours.append(coordinate[row-1][col]) # add left node to neighbour list
    
    
    
    
