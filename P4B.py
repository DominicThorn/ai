from collections import deque

def is_safe(m_left, c_left, m_right, c_right):
    if m_left > 0 and c_left > m_left:
        return False
    if m_right > 0 and c_right > m_right:
        return False
    return True

def missionaries_cannibals():
    start = (3, 3, 'L')
    goal = (0, 0, 'R')
    moves = [(2, 0), (0, 2), (1, 1), (1, 0), (0, 1)]
    queue = deque([(start, [start])])
    visited = set()
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal:
            return path
            
        if current_state in visited:
            continue
            
        visited.add(current_state)
        
        m_left, c_left, boat = current_state
        
        if boat == 'L':
            for m, c in moves:
                new_m_left = m_left - m
                new_c_left = c_left - c
                
                if 0 <= new_m_left <= 3 and 0 <= new_c_left <= 3:
                    m_right = 3 - new_m_left
                    c_right = 3 - new_c_left
                    if is_safe(new_m_left, new_c_left, m_right, c_right):
                        new_state = (new_m_left, new_c_left, 'R')
                        if new_state not in visited:
                            queue.append((new_state, path + [new_state]))
        else:
            for m, c in moves:
                new_m_left = m_left + m
                new_c_left = c_left + c
                
                if 0 <= new_m_left <= 3 and 0 <= new_c_left <= 3:
                    m_right = 3 - new_m_left
                    c_right = 3 - new_c_left
                    if is_safe(new_m_left, new_c_left, m_right, c_right):
                        new_state = (new_m_left, new_c_left, 'L')
                        if new_state not in visited:
                            queue.append((new_state, path + [new_state]))
                            
    return None

solution = missionaries_cannibals()

print("Solution path:")
if solution:
    for state in solution:
        print(state)
else:
    print("No solution found.")
