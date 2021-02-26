from qset_lib import Rover
import lidar
import math
#from queue import PriorityQueue


rover=Rover()
grid_edge_cost = 1


def compute(x, y):
    pass

def heuristics(s_x, s_y):
    pass
    node_x = start_x - s_x
    node_y = start_y - s_y
    node_final = math.sqrt((node_x**2)+(node_y**2))

    return node_final
    
def get_g(s1):
    pass




