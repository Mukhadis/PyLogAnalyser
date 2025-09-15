import os  #  Allows Python to interact with the OS
import re  # Regular expression module
import time  # Time module
import shutil  # Access the machine stats
from collections import Counter  # Useful Counting module


def log_parsing(file: str, message: str):
    # open the file as f to read from and create o to write to
    with open(file) as f, open("./logs/alerts.log", "w") as o:
        for line in f:  # Iterate through each line of the file
            if message in line:  # If the message is in the line
                o.write(line)


def count_occurrences(file: str):
    # pattern to find the type of error
    pattern = r"\b[0-9]{1,2} [A-Za-z]{1,10} ([A-Za-z]{1,20})\b"
    error_type_re = re.compile(pattern)  #  Regular expression

    with open(file) as f:
        load_data = f.read()  # Contents of the file stored in load_data

    #  Find all the matching error types in the file
    error_types = error_type_re.findall(load_data)

    #  Put Error types into Counter to use the most common function
    counted_error_types = Counter(error_types)

    for error, count in counted_error_types.most_common():
        print(f"{error}: {count}")


def cause_code_occurrences(file: str):
    #  Pattern to find cause codes
    pattern = r"\b[2-5]{1,3}\b"
    cause_code_re = re.compile(pattern)  #  Regular expression

    with open(file) as f:
        load_data = f.read()  # Contents of the file stored in load_data

    #  Final all the matching cause codes in the file
    cause_codes = cause_code_re.findall(load_data)

    #  Put cause code types into Counter to use the most common function
    counted_cause_codes = Counter(cause_codes)

    for code, count in counted_cause_codes.most_common():
        print(f"{code}: {count}")
