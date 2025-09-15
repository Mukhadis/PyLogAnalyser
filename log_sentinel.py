import utils


file = "logs/server.log"
message = "ERROR"

print("Error Summary:")
utils.count_occurrences(file)
print("\n")

print("HTTP Status Codes:")
utils.cause_code_occurrences(file)
