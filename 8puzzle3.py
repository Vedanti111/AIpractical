from collections import deque

# Define the initial and goal states
initial_state = [[1, 2, 3],
                 [4, 0, 5],
                 [6, 7, 8]]

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

# Possible moves
moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]

# Function to print the current state
def print_state(state):
    for row in state:
        print(' '.join(map(str, row)))
    print("\n")

# Find the blank space
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Check if the move is valid
def is_valid(x, y):
    return 0 <= x < 3 and 0 <= y < 3

# Apply the move to the state
def apply_move(state, move):
    x, y = find_blank(state)
    dx, dy = move
    if is_valid(x + dx, y + dy):
        new_state = [row[:] for row in state]
        new_state[x][y], new_state[x + dx][y + dy] = new_state[x + dx][y + dy], new_state[x][y]
        return new_state

# BFS to solve the puzzle
def bfs(initial_state):
    visited = set()
    queue = deque([(initial_state, [])])

    while queue:
        current_state, path = queue.popleft()
        visited.add(tuple(map(tuple, current_state)))

        if current_state == goal_state:
            return path

        for move in moves:
            new_state = apply_move(current_state, move)
            if new_state and tuple(map(tuple, new_state)) not in visited:
                new_path = path + [move]
                queue.append((new_state, new_path))

    return None

# Get the solution path
solution_path = bfs(initial_state)

# Print each step of the solution
current_state = initial_state
print("Initial State:")
print_state(current_state)

for move in solution_path:
    current_state = apply_move(current_state, move)
    print("Move:", move)
    print_state(current_state)