import json
import random

# Define rooms and devices for generating descriptions
rooms = ["Bedroom 1", "Bedroom 2", "Living Room", "Dining Room"]
devices = {
    "Bedroom 1": ["Smart Light", "Door Sensor", "Window Sensor", "Thermostat", "Ceiling Fan"],
    "Bedroom 2": ["Lamp", "Air Purifier", "Smart Bed", "Window Sensor", "Door Sensor"],
    "Living Room": ["TV", "Speaker", "Smart Light", "Window Sensor", "Door Sensor"],
    "Dining Room": ["Chandelier", "Smart Light", "Thermostat", "Smart Speaker", "Window Sensor"]
}

actions = ["turn on", "turn off", "activate", "deactivate", "start", "stop", "set to"]
conditions = ["when the door opens", "when the window closes", "at sunset", "at sunrise", "when motion is detected", "when temperature is above"]

# Generate Dataset 1: General to Detailed Description
dataset_1 = []

for i in range(100):
    room = random.choice(rooms)
    device = random.choice(devices[room])
    condition = random.choice(conditions)
    
    general_description = f"Imagine you are in the {room.replace(' 1', '').replace(' 2', '')}. You want the {device} to {random.choice(actions)} {condition}."
    detailed_description = f"In {room}, {condition.replace('the ', '').capitalize()}, the {device} should {random.choice(actions)}."
    
    entry = {
        "instruction": general_description,
        "output": detailed_description
    }
    dataset_1.append(entry)

# Generate Dataset 2: Detailed Description to LTL Formula
dataset_2 = []

for entry in dataset_1:
    room = random.choice(rooms)
    device_action = entry['output'].split(", the ")[1]
    condition = entry['output'].split(", ")[0].lower()
    device = entry['output'].split(", the ")[1].split(" ")[-3]
    
    ltl_formula = f"G({condition.replace(' ', '_').replace('is_', '')}_in_{room.replace(' ', '_')} -> X({device_action.replace(' ', '_')}_in_{room.replace(' ', '_')}))"
    
    entry = {
        "instruction": entry['output'],
        "output": ltl_formula
    }
    dataset_2.append(entry)

# Save both datasets
output_file_1 = 'dataset_general_to_tap.json'
output_file_2 = 'dataset_tap_to_ltl.json'

with open(output_file_1, 'w') as file1:
    json.dump(dataset_1, file1, indent=4)

with open(output_file_2, 'w') as file2:
    json.dump(dataset_2, file2, indent=4)

print(f"Datasets saved as {output_file_1} and {output_file_2}")
