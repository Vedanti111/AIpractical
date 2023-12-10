# Define variables
courses = ['CourseA', 'CourseB']
rooms = ['Room1', 'Room2', 'Room3']
time_slots = ['8:00-10:00', '10:00-12:00', '1:00-3:00']

# Define constraints
def time_conflict(slot1, slot2):
    return slot1 != slot2

def room_requirements(course, room):
    if course == 'CourseA' and room == 'Room1':
        return False
    elif course == 'CourseB' and room == 'Room3':
        return False
    return True

# Solve the problem
solutions = []
counter = 0
for slot1 in time_slots:
    for slot2 in time_slots:
        if time_conflict(slot1, slot2):
            for room1 in rooms:
                for room2 in rooms:
                    if room_requirements('CourseA', room1) and room_requirements('CourseB', room2):
                        solutions.append({'CourseA': (room1, slot1), 'CourseB': (room2, slot2)})
                        counter += 1
                        if counter >= 8:  # Limiting the solutions to 5
                            break
                if counter >= 8:
                    break
            if counter >= 8:
                break

# Print solutions
print("Solutions:")
for solution in solutions:
    print(solution)
