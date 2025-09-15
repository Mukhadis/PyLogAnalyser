import os  #  Allows Python to interact with the OS
import re  # Regular expression module
import time  # Time module
from collections import Counter  # Useful Counting module


def log_parsing(file: str, message: str):
    with open(file) as f:  # open the file
        for line in f:  # Iterate through each line of the file
            if message in line:
                return line.strip()
