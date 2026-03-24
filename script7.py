# Define two sets
set_names = {"Alice", "Bob", "Charlie", "Diana"}
subset_names = {"Alice", "Bob"}

# Check if set_names is a superset of subset_names
if set_names.issuperset(subset_names):
    print("set_names contains all names in subset_names.Alice Bob ")
else:
    print("set_names does NOT contain all names in subset_names.")
