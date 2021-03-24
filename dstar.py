import math
import heapq
from priority import PriorityQueue

class DStar:

    def __init__(self,start,goal,world_grid):
        self.start = start
        self.position = start
        self.goal = goal
        self.km = 0
        self.world_grid = world_grid #world grid from main
        self.open_set = PriorityQueue() #initialize priority queue with start node only
        self.rhs = [[float('inf') for x in range (len(self.world_grid[0]))] for y in range (len(self.world_grid))] #2d array same as world grid but with infinity values
        self.g = [[float('inf') for x in range (len(self.world_grid[0]))] for y in range (len(self.world_grid))]
        self.rhs[self.goal[0]][self.goal[1]] = 0
        self.open_set.put(self.goal,self.computeKey(self.goal)) #copy of queue with node only (to keep track of whats inside the queue)
        self.sensed = [[0 for x in range (len(self.world_grid[0]))] for y in range (len(self.world_grid))]


    def get_shortest_path(self):
        #loop while queue is not empty and lowest key is less than start key or rhs does not equal g for start
        while not self.open_set.empty() and self.open_set.first_key() < self.computeKey(self.start) or self.g[self.start[0]][self.start[1]] < self.rhs[self.start[0]][self.start[1]]:
            key_old = self.open_set.first_key() #get node lowest in queue
            u = self.open_set.pop()#get lowest key
            key_new = self.computeKey(u) #get key of u
            s_list = self.neighbours(u) #neighbouring nodes

            if key_old < key_new: #if lowest key is less than key of u
                self.open_set.put(u,key_new) #add new key to queue

            elif self.g[u[0]][u[1]] > self.rhs[u[0]][u[1]]: #if overconsistent
                self.g[u[0]][u[1]] = self.rhs[u[0]][u[1]] #set g and rhs equal
                #loop thru all nodes s in neighbours list
                for s in s_list:
                    self.update_vertex(s) #call update_vertex for each s
                    
            #when locally inconsistent        
            else:
                self.g[u[0]][u[1]] = float('inf') #g is inf
                
                s_list.append(u) #add u to neighbour list
                for s in s_list: #loop thru neighbours and call update_vertex
                    self.update_vertex(s)

    #get key for sorting in queue
    def computeKey(self,s):
        key1 = min(self.g[s[0]][s[1]],self.rhs[s[0]][s[1]]) + self.heuristics(self.start,s)+self.km
        key2 = min(self.g[s[0]][s[1]],self.rhs[s[0]][s[1]])
        return (key1,key2)

    #get euclidean distance estimate
    def heuristics(self,s,position): #distance from current node to start.
        x1,y1 = position
        x2,y2 = s
        node_x = abs(x1-x2)
        node_y = abs(y1-y2)
        node_final = math.sqrt((node_x**2)+(node_y**2))
        
        return node_final

    #cost of movement from u to s
    def cost(self,u,s):
        x1,y1 = u
        x2,y2 = s
        
        #if obstacle is at either node, cost is inf 
        if(self.sensed[x1][y1] == float('inf') or self.sensed[x2][y2] == float('inf')):
            return float('inf')
        #if obstacles are adjacent to either node, cost is high
        elif(self.sensed[x1][y1] == 2000 or self.sensed[x2][y2] == 2000):
            return float(100000000000000)
        else:
            return self.heuristics(u,s)

    #look for successors or predecessors of node u
    def neighbours(self,u):
        x,y = u
        #list of all possible 8 neighbouring nodes
        nodes_near = [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
        filtered = []
        #check if said neighbouring node exists in original node list
        for s in nodes_near:
            if s[0] >= 0 and s[0] < len(self.world_grid[0]) and s[1] >= 0 and s[1] < len(self.world_grid):
                filtered.append(s) #if it does, add to a new list with only existing neighbours
        return filtered 

    #update nodes in queue and their costs
    def update_vertex(self,u):
        #if we are not on the goal node
        if u != self.goal:
            #get the neighbouring nodes of u
            nodes_near = self.neighbours(u)
            lowest_cost = float('inf')

            for s in nodes_near:
                #if total cost from u to s is lower than predicted min cost
                if self.cost(u,s) + self.g[s[0]][s[1]] < lowest_cost:
                    #update lowest cost 
                    lowest_cost = self.cost(u,s) + self.g[s[0]][s[1]]
            
            #once the final lowest lookahead g(u) is found, update rhs 
            self.rhs[u[0]][u[1]]=lowest_cost
        #remove from queue   
        self.open_set.delete(u)
        
        #if node cost has been changed, place back in queue
        if self.g[u[0]][u[1]] != self.rhs[u[0]][u[1]]:
            self.open_set.put(u,self.computeKey(u))
    
    #get list of nodes near the start up to specified number of nodes ahead
    def sense_map(self,span):
        nodes_sensed = []
        row = len(self.world_grid)
        col = len(self.world_grid[0])
        
        for i in range (-span,span+1):
            for j in range(-span,span+1):
                if(self.start[0]+i >=0 and self.start[0]+i < row and self.start[1] + j >= 0 and self.start[1] + j < col):
                    if not (i == 0 and j == 0):
                        nodes_sensed.append((self.start[0]+i,self.start[1]+j))
        return nodes_sensed
