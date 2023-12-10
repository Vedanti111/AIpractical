from queue import Queue

def water_jug_problem(jug1_capacity, jug2_capacity, target_amount):
    visited_states = set()
    initial_state = (0, 0)  # Initial state: both jugs are empty
    queue = Queue()
    queue.put((initial_state, []))  # Add an empty list for steps

    while not queue.empty():
        current_state, steps = queue.get()
        jug1, jug2 = current_state

        if jug1 == target_amount or jug2 == target_amount:
            return steps  # Return the steps to reach the solution

        # Generate possible next states
        next_states = []

        # Fill jug1
        next_states.append(((jug1_capacity, jug2), steps + ["Fill jug1"]))

        # Fill jug2
        next_states.append(((jug1, jug2_capacity), steps + ["Fill jug2"]))

        # Empty jug1
        next_states.append(((0, jug2), steps + ["Empty jug1"]))

        # Empty jug2
        next_states.append(((jug1, 0), steps + ["Empty jug2"]))

        # Pour from jug1 to jug2
        pour_amount = min(jug1, jug2_capacity - jug2)
        next_states.append(((jug1 - pour_amount, jug2 + pour_amount), steps + [f"Pour jug1 to jug2 ({pour_amount})"]))

 # Pour from jug2 to jug1
        pour_amount = min(jug2, jug1_capacity - jug1)
        next_states.append(((jug1 + pour_amount, jug2 - pour_amount), steps + [f"Pour jug2 to jug1 ({pour_amount})"]))

        for next_state, next_steps in next_states:
            if next_state not in visited_states:
                visited_states.add(next_state)
                queue.put((next_state, next_steps))

    return None  # No solution found

jug1_capacity = 7
jug2_capacity = 3
target_amount = 5

solution_steps = water_jug_problem(jug1_capacity, jug2_capacity, target_amount)
if solution_steps:
    print("Steps to reach the solution:")
    for step in solution_steps:
      print(step)
else:
    print("No solution found.")