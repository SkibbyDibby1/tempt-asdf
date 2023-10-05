file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.rstrip()
        if any(word in line for word in ["flipped", "toggled", "reversed", "inverted", "switched"]):
            if "safe" in line:
                line = line.replace("safe", "unsafe")
            elif "unsafe" in line:
                line = line.replace("unsafe", "safe")
        print(line)

    safe_line_numbers = [str(line_number) for line_number, line in enumerate(lines, start=1) if line.startswith("safe")]
    if safe_line_numbers:
        print("Lines starting with 'safe' found at line numbers:", ", ".join(safe_line_numbers))
    else:
        print("No lines starting with 'safe' found.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
