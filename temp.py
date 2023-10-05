file_name = "03_trap_logs.txt"

try:
    with open(file_name, "r") as file:
        lines = file.readlines()

    for line_number, line in enumerate(lines, start=1):
        line = line.rstrip()
        line_parts = line.split(":")
        if len(line_parts) > 1:
            number_part = line_parts[0].strip()
            rest_part = ":".join(line_parts[1:]).strip()
            print(f"{number_part}: {rest_part}")
        else:
            print(line)

    line_numbers = [line_parts[0].strip() for line_parts in [line.split(":") for line in lines] if len(line_parts) > 1]
    if line_numbers:
        print("Numbers at the beginning of lines:", ", ".join(line_numbers))
    else:
        print("No lines with numbers at the beginning found.")

except FileNotFoundError:
    print(f"File '{file_name}' not found.")
