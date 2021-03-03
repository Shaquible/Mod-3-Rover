#from qset_lib import Rover
import lidar
import math
from grid import Grid
from queue import PriorityQueue


#rover=Rover()
grid_edge_cost = 1

def __init__(self,start,goal):
    pass
    self.start = start
    self.goal = goal
    self.g = float('inf')
    self.km = 0
    self.rhs = float('inf') #0 for the goal node

def calculateKey(self,s):
    pass
    key = [0,0]
    key[0] = min(g[s],rhs[s]) + heuristics(self.start,s)+km
    key[1] = min(g[s],rhs[s])
    return key

def compute(x, y):
    pass

def heuristics(s_x, s_y):
    pass
    node_x = abs(start_x - s_x)
    node_y = abs(start_y - s_y)
    node_final = math.sqrt((node_x**2)+(node_y**2))
    #must be 0 for start node
    return node_final
    
def get_g(s):
    pass

def get_rhs(s):
    pass