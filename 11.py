# Step 1: Read hammer collection from file and store in a dictionary
hammer_collection = {}
with open("hammer_collection.txt", "r") as file:
    for line in file:
        segments = line.strip().split("->")
        input_segment = segments[0].strip()
        output_segments = segments[1].strip().split()
        hammer_collection[input_segment] = output_segments

# Step 2: Read recipes from recipe book
recipes = []
with open("11_keymaker_recipe.txt", "r") as file:  # Replace "11_keymaker_recipe.txt" with the actual file name
    for line in file:
        recipe = line.strip().split(" - ")
        recipes.append(recipe)

# Step 3: Iterate through recipes and check for validity
valid_recipe = None
for recipe in recipes:
    valid = True
    key = list("A" * len(recipe))  # Initialize the key variable
    for step in recipe:
        hammer_index, position = map(int, step.strip("()").split(", "))
        segment = key[position - 1]  # Get the segment at the specified position
        if segment not in hammer_collection or hammer_index > len(hammer_collection[segment]):
            valid = False
            break
    if valid:
        valid_recipe = recipe
        break

if valid_recipe:
    # Step 4: Apply valid recipe to key segments
    key = list("A" * len(valid_recipe))
    for step in valid_recipe:
        hammer_index, position = map(int, step.strip("()").split(", "))
        segment = key[position - 1]
        new_segments = hammer_collection[segment]
        key[position - 1] = new_segments[hammer_index - 1]

    # Step 5: Final key segment
    final_key = "".join(key)
    print("The key that can open the chest is:", final_key)
else:
    print("No valid recipe found. Unable to open the chest.")
