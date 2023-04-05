# Python Scripting
# Can talk to other languages and software easily
# Large community
# Many libraries and easy to understand.

# Why we care about scripting?
# Automate repetitive manual tasks using code.

# Examples of python scripts as DevOps Engineer:
# Query a database.
# Execute a shell command.
# Create a backup.
# Fetch IP addresses of an autoscaling.
# check expiry date of an SSL certificate. (security of a website)

# 7 in built modules allowing us to do interesting things:
# sys (system)
# os (operating system)
# subprocess (interact with
# math
# random
# datetime
# json

# sys module
# import sys
# print(sys.version)  # Python version
#
# # os module
# import os
# print(os.getcwd())  # Current working directory
# # os.chdir()  # Change directory
# os.mkdir()  # Make new directory

# subprocess module
import subprocess
# Be careful not to create infinite loop. (Automate only after happy with manual process).
subprocess.run(["python", "hello_world.py"])

#math module
import math
pi = math.pi
pi_string = str(pi)
print(f"The value of pi is {pi_string}")

# random module
import random
random = random.randrange(1, 10)
print(random)

# datetime module
import datetime
what_is_the_date = datetime.datetime.now()
print(what_is_the_date)

# json module (use to transport data between systems
import json
x = {
    "name": "Samuel",
    "age": 30,
    "city": "London"
}

y = json.dumps(x)
print(y)  # Comes back as a string.