file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.rstrip()
        if any(word in line for word in ["flipped", "toggled", "reversed", "inverted", "switched"]):
            if line.endswith("safe"):
                line_parts = line.split(":")
                if len(line_parts) > 1:
                    print(line_parts[0].strip(), ":", line_parts[1].strip())
                else:
                    print(line)
            else:
                if "safe" in line:
                    line = line.replace("safe", "unsafe")
                elif "unsafe" in line:
                    line = line.replace("unsafe", "safe")
                print(line)
        else:
            print(line)

    safe_line_numbers = [line_parts[0].strip() for line_number, line in enumerate(lines, start=1) if line.endswith("safe") and ":" in line for line_parts in [line.split(":")]]
    if safe_line_numbers:
        print("Numbers at the beginning of lines ending with 'safe':", ", ".join(safe_line_numbers))
    else:
        print("No lines ending with 'safe' found.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
