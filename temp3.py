file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip()
            if any(word in line for word in ["flipped", "toggled", "reversed", "inverted", "switched"]):
                if "safe" in line:
                    line = line.replace("safe", "unsafe")
                elif "unsafe" in line:
                    line = line.replace("unsafe", "safe")
            print(line)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
