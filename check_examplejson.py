import fileinput
import os
import sys
import json

if len(sys.argv) > 1:
    if os.path.exists(sys.argv[1]):
        file = open(sys.argv[1], "r")
        json.load(file)
        file.close()
        print("JSON is valid!")
    else:
        print(sys.argv[1] + " not found")
else:
    print("usage: check_examplejson.py <file>")

# check_examplejson.py example.json = Terminal input to check if json file valid
