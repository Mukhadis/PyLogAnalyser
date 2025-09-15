import os  #  Allows Python to interact with the OS
import re  # Regular expression module
import time  # Time module
from collections import Counter  # Useful Counting module


def log_parsing(file: str, message: str):
    # open the file as f to read from and create o to write to
    with open(file) as f, open("./logs/alerts.log", "w") as o:
        for line in f:  # Iterate through each line of the file
            if message in line:  # If the message is in the line
                o.write(line)
