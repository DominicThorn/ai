def objective_function(x):
    return - (x - 5)**2 + 25

def hill_climbing(start):
    current = start
    
    while True:
        current_value = objective_function(current)
        left = current - 1
        right = current + 1
        
        left_value = objective_function(left)
        right_value = objective_function(right)
        
        if left_value > current_value:
            current = left
        elif right_value > current_value:
            current = right
        else:
            break
            
    return current, objective_function(current)

start = 0
state, value = hill_climbing(start)

print("Final State: ", state)
print("Maximum Value:", value)