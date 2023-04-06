import json
import os
import sys
import yaml

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        yaml.safe_load(file.read())
        file.close()
        print("YAML is valid!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("usage: example.yaml <file>")

# python3 check_yaml_file_is_valid.py example.yaml - Terminal input to check yaml file is valid.
