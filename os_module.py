# OS Module

import os
# Prints message to terminal
os.system('echo "Hello World!"')

# OS module to manipulate directories (folders)
import shutil

#Directory
directory = "test_dir"

# Path to parent directory (Where it's being made)
parent_dir = "/Users/samuelnaiwo/Documents"

# Path
path = os.path.join(parent_dir, directory)

# # Create the directory
# os.mkdir(path)
# print("Directory '% s' created" % directory)

# Put a file in the new directory (folder)
filename = "testfile.txt"
filepath = os.path.join(path, filename)

with open(os.path.join(path, filename), "w") as file1:
    toFile = "content of the file is written here"
    file1.write(toFile)
print(f"File " + filename + " created in " + directory + " folder")