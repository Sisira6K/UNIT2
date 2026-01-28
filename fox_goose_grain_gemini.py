from collections import deque

def is_valid(state):
    farmer, fox, goose, grain = state
    # If fox and goose are together without the farmer
    if fox == goose and farmer != fox:
        return False
    # If goose and grain are together without the farmer
    if goose == grain and farmer != goose:
        return False
    return True

def get_neighbors(state):
    neighbors = []
    farmer, fox, goose, grain = state
    
    # Possible items the farmer can take (including taking nothing/None)
    items = [None, 'fox', 'goose', 'grain']
    
    for item in items:
        new_state = list(state)
        # The farmer always moves
        new_state[0] = not farmer
        
        # Move the chosen item if it's on the same side as the farmer
        if item == 'fox' and fox == farmer:
            new_state[1] = not fox
        elif item == 'goose' and goose == farmer:
            new_state[2] = not goose
        elif item == 'grain' and grain == farmer:
            new_state[3] = not grain
        elif item is not None:
            continue # Farmer can't take an item that isn't on their side
            
        new_state_tuple = tuple(new_state)
        if is_valid(new_state_tuple):
            neighbors.append(new_state_tuple)
    return neighbors

def solve():
    start_state = (False, False, False, False) # All on near side
    goal_state = (True, True, True, True)      # All on far side
    
    queue = deque([(start_state, [])])
    visited = {start_state}
    
    while queue:
        current_state, path = queue.popleft()
        
        if current_state == goal_state:
            return path + [goal_state]
            
        for neighbor in get_neighbors(current_state):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [current_state]))
    return None

def format_state(state):
    names = ["Farmer", "Fox", "Goose", "Grain"]
    near = [names[i] for i in range(4) if not state[i]]
    far = [names[i] for i in range(4) if state[i]]
    return f"Near: {near} | Far: {far}"

# Execute and print results
solution = solve()
if solution is None:
    print('No solution found.')
else:
    for i, step in enumerate(solution):
        print(f"Step {i}: {format_state(step)}")
