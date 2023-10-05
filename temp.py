file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            print(line.rstrip())
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
