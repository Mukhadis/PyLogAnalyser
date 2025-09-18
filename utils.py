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
    print(f"Log parsing complete. Check alerts.log for {message} messages.")


def count_occurrences(error_file: str):
    # pattern to find the type of error
    pattern = r"\bERROR ([A-Za-z]{1,20})\b"
    error_type_re = re.compile(pattern)  #  Regular expression

    if os.path.exists(error_file):
        with open(error_file) as f:  # Open the alerts file
            load_data = f.read()  # Contents of the file stored in load_data
        error_types = error_type_re.findall(load_data)
        counted_errors = Counter(error_types)
        for error, count in counted_errors.most_common():
            print(f"{error}: {count}")
    else:
        print("alerts.log does not exist. Please run log_parsing first.")


def cause_code_occurrences(file: str):
    #  Pattern to find cause codes
    pattern = r"\b=([0-5]{3})\b"
    cause_code_re = re.compile(pattern)  #  Regular expression

    with open(file) as f:
        load_data = f.read()  # Contents of the file stored in load_data

    #  Final all the matching cause codes in the file
    cause_codes = cause_code_re.findall(load_data)

    #  Put cause code types into Counter to use the most common function
    counted_cause_codes = Counter(cause_codes)

    for code, count in counted_cause_codes.most_common():
        print(f"{code}: {count}")


def log_rotate(error_file: str):
    current_path = "./logs/"  # The path where the alerts file resides
    current_files = os.listdir(current_path)  # Makes the directory as list
    for file in current_files:  # Iterate through the list
        if os.path.exists(error_file):  # If the file is there
            # Create a new file and copy the contents of current into the new
            with open(f"{error_file}.1", "w") as outfile, open(error_file) as infile:
                outfile.write(infile.read())
    # Create a new empty alerts.log
    with open("./logs/alerts.log", "w"):
        pass
    print("Log rotation complete.")


def disk_space():
    total = shutil.disk_usage("/").total  # Total amount of disk space
    free = shutil.disk_usage("/").free  # Free amount if disk space

    free_percent = int((free/total) * 100)  # Percentage of diskspace free

    if free_percent < 20:
        print("ALERT: Low disk space")
    else:
        print(f"Disk Free: {free_percent}%")


def delete_old_files(path: str):
    current_path = path  #  Path where the files are located
    files = os.listdir(current_path)  # List of files in the directory
    cut_off = 60  # Files older than 1 minute will be deleted
    current_time = time.time()  # Current time in seconds

    for file in files:
        file_path = os.path.join(current_path, file)
        if os.path.isfile(file_path):  # If it is a file
            mod_time = os.stat(file_path).st_mtime
            if current_time - mod_time > cut_off:
                os.remove(file_path)
                print(f"Deleting {file} as it is older than 1 minute")
            else:
                print(f"{file} is not older than 1 minute, skipping...")
