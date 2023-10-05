def is_ordered_key(key):
    # Iterate through each segment in the key
    for i in range(len(key) - 1):
        # Compare the current segment with the next segment
        if key[i] > key[i + 1]:
            return False
    return True

def find_ordered_key_from_file(file_path):
    # Read the keys from the file
    with open(file_path, 'r') as file:
        keys = file.read().splitlines()

    # Iterate through each key in the pile
    for key in keys:
        # Check if the key is ordered
        if is_ordered_key(key):
            return key

    # If no ordered key is found, return None or an appropriate value
    return None

# Example usage:
file_path = '01_keymaker_ordered.txt'

ordered_key = find_ordered_key_from_file(file_path)
if ordered_key:
    print("Ordered key found:", ordered_key)
else:
    print("No ordered key found in the pile.")
