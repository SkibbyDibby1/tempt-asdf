def is_trap_safe(log):
    deactivated_words = ['inactive', 'disabled', 'quiet', 'standby', 'idle']
    activated_words = ['live', 'armed', 'ready', 'primed', 'active']
    state_change_words = ['flipped', 'toggled', 'reversed', 'inverted', 'switched']
    
    # Split the log into individual words
    words = log.split()
    
    # Check if the trap is safe based on the last word in the log
    last_word = words[-1]
    
    if last_word in deactivated_words:
        return True
    elif last_word in activated_words:
        return False
    elif last_word in state_change_words:
        # Check the second last word to determine the previous state
        previous_state = words[-2]
        if previous_state in deactivated_words:
            return False
        elif previous_state in activated_words:
            return True
    
    # Return False if the last word is not recognized
    return False

def find_safe_traps(file_path):
    safe_traps = []
    
    # Read the trap logs from the file
    with open(file_path, 'r') as file:
        scan_results = file.read()
    
    # Split the scan results into individual lines
    lines = scan_results.split('\n')
    
    # Iterate through each line and check if the trap is safe
    for line in lines:
        trap_id, log = line.split(':')
        trap_id = trap_id.strip()
        log = log.strip()
        
        if is_trap_safe(log):
            safe_traps.append(trap_id)
    
    return safe_traps

# File path
file_path = '03_trap_logs.txt'

safe_traps = find_safe_traps(file_path)

print("Safe traps:", safe_traps)
