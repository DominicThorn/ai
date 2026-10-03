import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [start])]
    visited = set()
    
    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)
        
        if node in visited:
            continue
        
        visited.add(node)
        
        if node == goal:
            return path, cost
            
        for neighbour, edge_cost in graph[node]:
            if neighbour not in visited:
                heapq.heappush(priority_queue, (cost + edge_cost, neighbour, path + [neighbour]))
                
    return None, float("inf")

graph = {
    'A': [('B', 2), ('C', 5)],
    'B': [('A', 2), ('D', 4), ('E', 1)],
    'C': [('A', 5), ('F', 2)],
    'D': [('B', 4), ('G', 3)],
    'E': [('B', 1), ('G', 6)],
    'F': [('C', 2), ('G', 1)],
    'G': [('D', 3), ('E', 6), ('F', 1)]
}

start = 'A'
goal = 'G'

path, cost = uniform_cost_search(graph, start, goal)

print("Optimal Path: ", " -> ".join(path))
print("Total Cost: ", cost)
