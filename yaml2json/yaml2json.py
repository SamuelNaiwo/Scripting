import json
import os
import sys
import yaml

if len(sys.argv) > 1:
# Opening a file
    if os.path.exists(sys.argv[1]):
        source_file = open(sys.argv[1], "r")
        source_content = yaml.safe_load(source_file)
        source_file.close()
    # If file isn't found
    else:
        print(f"ERROR: ", {sys.argv[1]}, " not found")
        exit(1)
else:
    print("Wrong execution format")

# Processing the conversion
output = yaml.dump(source_content)

target_file = open(sys.argv[2], "w")
target_file.write(output)
target_file.close()

# python3 yaml2json.py example.yaml output.json - Terminal input to create new file.

