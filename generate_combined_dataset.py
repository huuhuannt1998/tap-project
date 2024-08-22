import json
import random

# Define rooms, devices, actions, and conditions for generating the dataset
rooms = ["Bedroom 1", "Bedroom 2", "Living Room", "Dining Room"]
devices = {
    "Bedroom 1": ["Smart Light", "Door Sensor", "Window Sensor", "Thermostat", "Ceiling Fan"],
    "Bedroom 2": ["Lamp", "Air Purifier", "Smart Bed", "Window Sensor", "Door Sensor"],
    "Living Room": ["TV", "Speaker", "Smart Light", "Window Sensor", "Door Sensor"],
    "Dining Room": ["Chandelier", "Smart Light", "Thermostat", "Smart Speaker", "Window Sensor"]
}

actions = ["turn on", "turn off", "activate", "deactivate", "start", "stop", "set to"]
conditions = ["when the door opens", "when the window closes", "at sunset", "at sunrise", "when motion is detected", "when temperature is above"]

# Generate a combined dataset
combined_dataset = []

for i in range(100):
    room = random.choice(rooms)
    device = random.choice(devices[room])
    action = random.choice(actions)
    condition = random.choice(conditions)
    
    natural_language_description = f"Imagine you are in the {room.replace(' 1', '').replace(' 2', '')}. You want the {device} to {action} {condition}."
    ltl_formula = f"G({condition.replace('the ', '').replace(' ', '_').replace('is_', '')}_in_{room.replace(' ', '_')} -> X({action.replace(' ', '_')}_{device.replace(' ', '_')}_in_{room.replace(' ', '_')}))"
    
    entry = {
        "instruction": natural_language_description,
        "output": ltl_formula
    }
    combined_dataset.append(entry)

# Save the combined dataset
output_file_combined = 'combined_dataset.json'

with open(output_file_combined, 'w') as file:
    json.dump(combined_dataset, file, indent=4)

print(f"Dataset saved as {output_file_combined}")
