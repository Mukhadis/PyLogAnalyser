import utils
import _datetime

file = "logs/server.log"
alerts_log = "logs/alerts.log"
message = "ERROR"

utils.log_parsing(file, message)
print("Error Summary:")
utils.count_occurrences(file)
print("\n")

print("HTTP Status Codes:")
utils.cause_code_occurrences(file)
print("\n")

utils.disk_space()
utils.log_rotate(alerts_log)
