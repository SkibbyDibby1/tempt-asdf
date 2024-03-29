# Step 1: Read hammer collection from file and store in a dictionary
hammer_collection = {}
with open("hammer_collection.txt", "r") as file:
    for line in file:
        segments = line.strip().split("->")
        input_segment = segments[0].strip()
        output_segment = segments[1].strip()
        if input_segment not in hammer_collection:
            hammer_collection[input_segment] = []
        hammer_collection[input_segment].append(output_segment)

# Step 2: Read recipes from recipe book
recipes = []
with open("11_keymaker_recipe.txt", "r") as file:
    for line in file:
        recipe = line.strip().split(" - ")
        recipes.append(recipe)

# Step 3: Iterate through recipes and check for validity
valid_recipe = None
for recipe in recipes:
    valid = True
    key = list("A" * len(recipe))  # Initialize the key variable

    # Step 4: Apply valid recipe to key segments
    for step in recipe:
        hammer_index, position = map(int, step.strip("()").split(", "))
        segment = key[position - 1] if position <= len(key) else None
        if segment not in hammer_collection or hammer_index > len(hammer_collection.get(segment, [])):
            valid = False
            break
        new_segment = hammer_collection[segment][hammer_index - 1]
        key[position - 1] = new_segment

    if valid:
        valid_recipe = recipe
        break

if valid_recipe:
    # Step 5: Final key segment
    final_key = "".join(key)
    print("The key that can open the chest is:", final_key)
else:
    print("No valid recipe found. Unable to open the chest.")
