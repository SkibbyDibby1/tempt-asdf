def is_trap_safe(log):
    safe_words = ["inactive", "disabled", "quiet", "standby", "idle"]
    unsafe_words = ["live", "armed", "ready", "primed", "active"]

    for word in log:
        if word in unsafe_words:
            return False
        elif word not in safe_words:
            return False

    return True

def find_safe_traps(log_file_path):
    with open(log_file_path, "r") as file:
        lines = file.readlines()

    safe_traps = []
    for line in lines:
        line = line.strip()
        if ":" in line:
            trap_id, log = line.split(": ")
        else:
            trap_id = line.split()[0]
            log = line.split()[1:]
        log = log.split()
        if is_trap_safe(log):
            safe_traps.append(int(trap_id))

    return safe_traps

# Usage example
log_file_path = "03_trap_logs.txt"
safe_traps = find_safe_traps(log_file_path)
print("Safe traps:", safe_traps)
