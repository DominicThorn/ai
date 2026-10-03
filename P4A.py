from collections import deque

def water_jug_problem(capacity_a, capacity_b, target):
    queue = deque([((0, 0), [])])
    visited = set()
    
    while queue:
        (a, b), path = queue.popleft()
        
        if (a, b) in visited:
            continue
            
        visited.add((a, b))
        
        if a == target or b == target:
            return path + [(a, b)]
            
        states = [
            ((capacity_a, b), "Fill Jug A"),
            ((a, capacity_b), "Fill Jug B"),
            ((0, b), "Empty Jug A"),
            ((a, 0), "Empty Jug B")
        ]
        
        # Pour A into B
        amount = min(a, capacity_b - b)
        states.append(((a - amount, b + amount), "Pour A into B"))
        
        # Pour B into A
        amount = min(b, capacity_a - a)
        states.append(((a + amount, b - amount), "Pour B into A"))
        
        for state, operation in states:
            if state not in visited:
                queue.append((state, path + [operation]))
                
    return None

capacity_a = 4
capacity_b = 3
target = 2

solution = water_jug_problem(capacity_a, capacity_b, target)

print("Solution: ")
if solution:
    for step in solution:
        print(step)
else:
    print("No solution exists.")