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

            words = line.split()
            if len(words) > 0:
                last_word = words[-1]
                if last_word == "safe":
                    colon_index = line.rfind(":")
                    if colon_index != -1:
                        number = line[colon_index - 1]
                        print(number)
            
            print(line)
except FileNotFoundError:
    print(f"File '{file_name}' not found.")
