from collections import deque

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    row = zero // 3
    col = zero % 3
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc
        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
            
    return neighbors

def number_puzzle(start, goal):
    queue = deque([(start, [start])])
    visited = {start}
    
    while queue:
        current, path = queue.popleft()
        
        if current == goal:
            return path
            
        for next_state in get_neighbors(current):
            if next_state not in visited:
                visited.add(next_state)
                queue.append((next_state, path + [next_state]))
                
    return None

def display(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])

start = (1, 2, 3, 4, 0, 6, 7, 5, 8)
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

solution = number_puzzle(start, goal)
print("Number Puzzle Solution: ")
if solution:
    for step, state in enumerate(solution):
        print("Step", step)
        display(state)
else:
    print("No Solution found")