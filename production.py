class ProductionSystem:
    def __init__(self):
        self.rules = []

    def add_rule(self, condition, action):
        self.rules.append((condition, action))

    def infer(self, input_data):
        for condition, action in self.rules:
            if condition(input_data):
                return action
        return "No action found"

# Define conditions and actions
def is_cold(temp):
    return temp < 68

def is_hot(temp):
    return temp > 75

def adjust_heating(temp):
    return f"Increasing heating to {temp + 5} degrees."

def adjust_cooling(temp):
    return f"Increasing cooling to {temp - 5} degrees."

def do_nothing(temp):
    return "No action needed."

# Create a production system
thermostat_control = ProductionSystem()

# Add rules to the system
thermostat_control.add_rule(is_cold, adjust_heating)
thermostat_control.add_rule(is_hot, adjust_cooling)
thermostat_control.add_rule(lambda x: True, do_nothing)  # Default rule

# Input data (temperature)
temperature = int(input("Enter the temperature "))

# Perform inference and take action
result = thermostat_control.infer(temperature)
print(result)
