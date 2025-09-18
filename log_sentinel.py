import utils
import _datetime  # Access the date


path_to_logs = "logs/"
file = "logs/serverlogs/server.log"
error_file = "logs/alerts.log"
message = "ERROR"

print('''
Welcome to Log Sentinel:
      
Please read the below options to direct your requests:

1. Parse error messages and store seperately.
2. Print an error summary
3. Print HTTP status codes
4. Print disk space
5. Rotate Logs
6. Delete aged files
7. Quit
''')

while True:
    try:
        user_input = int(input())
        if user_input == 1:
            utils.log_parsing(file, message)
        elif user_input == 2:
            print("Error Summary:")
            utils.count_occurrences(error_file)
        elif user_input == 3:
            print("HTTP Status Codes:")
            utils.cause_code_occurrences(file)
        elif user_input == 4:
            utils.disk_space()
        elif user_input == 5:
            utils.log_rotate(error_file)
        elif user_input == 6:
            utils.delete_old_files(path_to_logs)
        elif user_input == 7:
            print("Exiting Log Sentinel. Goodbye!")
            break
        else:
            print("Invalid input, please enter a number between 1 and 7")

    except ValueError:
        print("Invalid input")
