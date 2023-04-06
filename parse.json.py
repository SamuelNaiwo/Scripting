import json
import os

# json = json.loads(open("/Users/samuelnaiwo/Documents/Tech 221/scripting/example.json").read())
# value = json["name"]
# print(value)

script_dir = os.path.dirname(__file__)  # __file__ - Current File
print("The script is located at: " + script_dir)

script_absolute_path = os.path.join(script_dir, "example.json")
print("The script path is: " + script_absolute_path)

# Script Parse
json = json.loads(open(script_absolute_path).read())
value = json["name"]
print(value)

# Loop through json keys and values
for key in json:
    print(key, ":", json[key])

for key in json:
    value = json[key]
    print(f"The key and values are {key}: {value}")