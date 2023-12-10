import random

# Define your objective function (heuristic)
def heuristic(x):
    # You should replace this with your specific heuristic function
    # It should return a higher value for better solutions
    return -x**2  # Example: Maximizing a simple quadratic function

# Hill Climbing algorithm
def hill_climbing(initial_solution, step_size, max_iterations):
    current_solution = initial_solution
    current_value = heuristic(current_solution)

    for i in range(max_iterations):
        # Generate a neighboring solution by adding or subtracting the step size
        neighbor = current_solution + random.uniform(-step_size, step_size)

        # Calculate the heuristic value of the neighbor
        neighbor_value = heuristic(neighbor)

        # If the neighbor is better, move to it
        if neighbor_value > current_value:
            current_solution = neighbor
            current_value = neighbor_value

    return current_solution, current_value

if __name__ == '__main__':
    # Parameters
    initial_solution = 2.0  # Starting point
    step_size = 0.1  # Size of steps to take
    max_iterations = 100

    final_solution, final_value = hill_climbing(initial_solution, step_size, max_iterations)
    print("Final Solution:", final_solution)
    print("Final Value:", final_value)
