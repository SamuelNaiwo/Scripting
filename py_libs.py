# Python Libraries and Modules

# Extensive Libraries - External collections of usual functions and methods

# Python comes with some integrated libraries

import random

print(random.random())  # Gives random float between 0-1

from random import *

print(random())  # Quicker to use. * imports all the methods

import math

num_float = 23.66
print(math.ceil(num_float))
print(math.floor(num_float))

# Modules
# A module is a set of code or function with the .py extension.

import os  # Operating system

working_dir = os.getcwd()  # Current Working Directory
print(working_dir)

import datetime, sys  # Can us comma to import different modules.
print(datetime.date.today())
print(sys.path)

def operating_system_information():
    print(os.cpu_count())

operating_system_information()

# pip - Python Package Manager
import requests

requests_bbc = requests.get("https://www.bbc.co.uk")

print(requests_bbc.content)