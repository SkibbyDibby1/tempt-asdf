file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            if any(word in line for word in ["inactive", "disabled", "quiet", "standby", "idle"]):
                line += " safe"
            print(line)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
