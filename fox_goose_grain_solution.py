# Fox, Goose, and Grain river crossing solution
# State: (farmer, fox, goose, grain), 0=left, 1=right
from collections import deque

def is_valid(state):
    f, x, g, r = state
    # If farmer is not with goose, fox and goose can't be together
    if f != g and x == g:
        return False
    # If farmer is not with goose, goose and grain can't be together
    if f != g and g == r:
        return False
    return True

def get_moves(state):
    f, x, g, r = state
    moves = []
    # Farmer crosses alone
    new_state = (1-f, x, g, r)
    if is_valid(new_state):
        moves.append((new_state, 'Farmer crosses alone'))
    # Farmer takes fox
    if x == f:
        new_state = (1-f, 1-x, g, r)
        if is_valid(new_state):
            moves.append((new_state, 'Farmer takes fox'))
    # Farmer takes goose
    if g == f:
        new_state = (1-f, x, 1-g, r)
        if is_valid(new_state):
            moves.append((new_state, 'Farmer takes goose'))
    # Farmer takes grain
    if r == f:
        new_state = (1-f, x, g, 1-r)
        if is_valid(new_state):
            moves.append((new_state, 'Farmer takes grain'))
    return moves

def solve():
    start = (0, 0, 0, 0)
    goal = (1, 1, 1, 1)
    queue = deque()
    queue.append((start, []))
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)
        for new_state, action in get_moves(state):
            queue.append((new_state, path + [(new_state, action)]))
    return None

if __name__ == "__main__":
    solution = solve()
    if solution:
        print('Solution found:')
        for idx, (state, action) in enumerate(solution, 1):
            print(f"Step {idx}: {action} -> State: {state}")
    else:
        print('No solution found.')
"""
Fox, Goose, and Grain River Crossing Puzzle Solution

This script prints the optimal sequence of moves to solve the classic puzzle.
"""

def print_solution():
    steps = [
        "1. Farmer takes the goose across the river.",
        "2. Farmer returns alone.",
        "3. Farmer takes the fox across the river.",
        "4. Farmer brings the goose back.",
        "5. Farmer takes the grain across the river.",
        "6. Farmer returns alone.",
        "7. Farmer takes the goose across the river."
    ]
    print("Fox, Goose, and Grain River Crossing Solution:\n")
    for step in steps:
        print(step)
    print("\nAll items have been safely transported!")

if __name__ == "__main__":
    print_solution()
