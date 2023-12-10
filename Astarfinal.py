import heapq

class Node:
    def __init__(self, state, parent, cost, heuristic):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic
        self.total_cost = cost + heuristic

    def __lt__(self, other):
        return self.total_cost < other.total_cost

def search(graph, start, goal, heuristic):
    open_list = []
    closed_set = set()

    initial_node = Node(start, None, 0, heuristic(start))
    heapq.heappush(open_list, initial_node)

    while open_list:
        current_node = heapq.heappop(open_list)
        current_state = current_node.state

        if current_state == goal:
            return path_to_goal(current_node)

        closed_set.add(current_state)

        for neighbor, cost in graph[current_state]:
            if neighbor not in closed_set:
                child_node = Node(
                    neighbor,
                    current_node,
                    current_node.cost + cost,
                    heuristic(neighbor)
                )
                heapq.heappush(open_list, child_node)

    return None  # No solution found

def path_to_goal(node):
    path = []
    while node:
        path.append(node.state)
        node = node.parent
    return list(reversed(path))

# Example usage:
if __name__ == "__main__":
    # Define your graph and heuristic function
    graph = {
        'S': [('A', 1),('G', 12)],
        'A': [('B', 3), ('C', 1)],
        'B': [('D', 3)],
        'C': [('D', 1), ('G',2)],
        'D': [('G', 3)],
        'G': []
    }

    def heuristic(state):
        # Define your heuristic function based on the problem
        heuristic_values = {'S': 4, 'A':2, 'B': 6, 'C': 2, 'D': 3, 'G': 0}
        return heuristic_values[state]

    start = 'S'
    goal = 'G'

    solution = search(graph, start, goal, heuristic)
    print("Solution path:", solution)
