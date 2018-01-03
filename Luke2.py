from time import time
from collections import defaultdict
from collections import deque

def labyrinth_to_graph(labyrinth):
    """
    Given a labyrinth where '# ' are walls and '_ ' are non-wall cells, 
    construct a graph where all non-wall cells are nodes and the edges are the 
    neighboring non-wall cells
    """
    # Get dimensions of labyrinth
    x_dim = len(labyrinth[0])
    y_dim = len(labyrinth)
    
    # Create names for the nodes representing the cells in the labyrinth
    node = 1
    nodes = []
    for y in range(y_dim):
        nodes.append([])
        for x in range(x_dim):
            if labyrinth[y][x] == '_ ':
                nodes[y].append(node)
                node += 1
            else:
                nodes[y].append('#')
    
    # Go through the labyrinth to create edges for the graph
    graph = defaultdict(list)
    for y in range(y_dim):
        for x in range(x_dim):
            
            # Find all non-wall neighboring cells
            edges = neighbors(x, y, labyrinth, x_dim, y_dim)
            
            # If there are no non-wall neighboring cells
            if not edges:
                graph[nodes[y][x]] = []
                
            # Create edges for all neighboring cells
            for edge in edges:
                x_edge, y_edge = edge
                graph[nodes[y][x]].append(nodes[y_edge][x_edge])

    return graph

def neighbors(x, y, labyrinth, x_dim, y_dim):
    """
    Finds all non-wall neighboring cells of current cell, and returns their
    coordinates
    """
    neighbors = []
    
    # Can we move up?
    if y > 0 and labyrinth[y-1][x] == '_ ':
        neighbors.append((x,y-1))
        
    # Can we move down?
    if y < y_dim - 1 and labyrinth[y+1][x] == '_ ':
        neighbors.append((x,y+1))
    
    # Can we move to the left?
    if x > 0 and labyrinth[y][x-1] == '_ ':
        neighbors.append((x-1,y))
    
    # Can we move to the right?
    if x < x_dim - 1 and labyrinth[y][x+1] == '_ ':
        neighbors.append((x+1,y))
        
    return neighbors

def labyrinth_generator(x_dim, y_dim):
    """
    Generates a labyrint from given dimensions, and where '# ' represents
    walls and '_ ' represent non-wall cells.
    """
    # Create labyrinth with no walls
    labyrinth = [['_ ' for x in range(x_dim)] for y in range(y_dim)]

    # Go through labyrinth to put up walls
    for y in range(y_dim):
        for x in range(x_dim):
            
            # Check if there should be a wall in this cell
            if wall(x,y):
                labyrinth[y][x] = '# '
    
    return labyrinth

def wall(x,y):
    """
    Function that decides if a wall should be put up or not. If there is an odd 
    number of ones in the binary representation of the output of the function
    f(x,y) = x**3 + 12*x*y + 5*x*y**2, then there should be put up a wall 
    (return True), and if there is an even number then there should not be put
    up a wall (return False)
    """
    
    # Since coordinates start on 0
    x += 1
    y += 1
    
    if sum(int(i) for i in bin(x**3 + 12*x*y + 5*x*y**2)[2:]) % 2 == 0:
        return False
    else:
        return True
    
def BFS(graph, start_node):
    """
    Breadth first search
    """
    
    # Mark all nodes as not visited
    visited = dict()
    for node in graph.keys():
        if node != '#':
            visited[node] = False
    
    # Mark start node as visited
    visited[start_node] = True
    
    # Put neighbors of start node into queue
    queue = deque()
    for neighbor in graph[start_node]:
        queue.append(neighbor)
    
    # Start the search
    while queue:
        
        node = queue.popleft()
        visited[node] = True
        
        # Put all neighbors into queue
        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
    
    return visited

#-----------------------------------------------------------------------------#
#---------------------------------- M A I N ----------------------------------#
#-----------------------------------------------------------------------------#

start_time = time()

# Dimensions of labyrint
x_dim = 1000
y_dim = 1000

# Create labyrint
print('> Creating labyrinth')
labyrinth = labyrinth_generator(x_dim, y_dim)

# Turn labyrinth into graph, where each cell (which is not a wall) is a node,
# and the edges are the possible moves between the nodes
print('> Creating graph')
graph = labyrinth_to_graph(labyrinth)

# Run BFS on the graph to find which nodes are reachable
print('> Running BFS')
start_node = 1
visited = BFS(graph, start_node)

# Count the number of nodes that are not reachable from the start-node
print('> Counting number of non-visited nodes')
non_visited = 0
for key,value in visited.items():
    if value == False:
        non_visited += 1

# Print solution
print('Solution:', non_visited)
print('Time:', time() - start_time)
