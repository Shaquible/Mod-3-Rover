from qset_lib import Rover
import lidar
import math
from queue import PriorityQueue


rover=Rover()
grid_edge_cost = 1

def __init__(self,start,target):
    pass
    self.start = start
    self.g = inf
    self.km = 0
    self.rhs = inf #0 for the goal node

def computeKey(s, start_node):
    pass
    key1 = min(g[s],rhs[s]) + heuristics(start_node,s)+km
    key2 = min(g[s],rhs[s])
    return key1,key2

def compute(x, y):
    pass

def heuristics(s_x, s_y):
    pass
    node_x = abs(start_x - s_x)
    node_y = abs(start_y - s_y)
    node_final = math.sqrt((node_x**2)+(node_y**2))
    #must be 0 for start node
    return node_final
    
def get_g(s1):
    pass

def get_rhs(s):
    pass