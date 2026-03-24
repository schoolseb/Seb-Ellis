CAPACITY = 5


# Function to add a new animal to the shelter
def add_animal(animal_list, name, species, capacity):
    """
    Adds a new animal to the shelter list if the capacity has not been reached.

    Parameters:
        animal_list (list): The current list of animals (each animal is a dict).
        name (str): Name of the animal to add.
        species (str): Species of the animal to add.
        capacity (int): Maximum number of animals the shelter can hold.

    Returns:
        bool: True if the animal was added, False if capacity reached.
    """
    if len(animal_list) < capacity:

        animal_list.append({"name": name, "species": species})
        print(f"{name} the {species} added.")
        return True
    else:
        print("Cannot add more animals. Capacity reached.")
        return False


# Function to remove an animal from the shelter by name when adopted
def adopt_animal(animal_list, name):
    """
    Removes an animal from the shelter list by name.

    Parameters:
        animal_list (list): The current list of animals.
        name (str): Name of the animal to adopt.

    Returns:
        bool: True if an animal was adopted, False if not found.
    """
    for animal in animal_list:
        if animal["name"] == name:
            animal_list.remove(animal)
            print(f"{name} has been adopted. Hooray!")
            return True
    print(f"No animal named {name} found.")
    return False


# Function to get the total number of animals in the shelter
def get_animal_count(animal_list):
    """
    Returns the total number of animals in the shelter list.

    Parameters:
        animal_list (list): The current list of animals.

    Returns:
        int: Number of animals in the list.
    """
    return len(animal_list)


# Example usage
if __name__ == "__main__":

    # Create a new shelter list
    shelter_animals = []

    # Add animals to the shelter
    add_animal(shelter_animals, "Buddy", "Dog", CAPACITY)
    add_animal(shelter_animals, "Whiskers", "Cat", CAPACITY)
    add_animal(shelter_animals, "Nemo", "Fish", CAPACITY)

    # Display total animals
    print("Total animals in shelter:", get_animal_count(shelter_animals))

    # Adopt an animal
    adopt_animal(shelter_animals, "Whiskers")

    # Display total animals after adoption
    print("Total animals in shelter after adoption:", get_animal_count(shelter_animals))

    # Attempt to add more animals beyond capacity
    add_animal(shelter_animals, "Tiger", "Tiger", CAPACITY)
    add_animal(shelter_animals, "Elephant", "Elephant", CAPACITY)
    add_animal(shelter_animals, "Giraffe", "Giraffe", CAPACITY)

    # Final list of animals
    print("Final animals in shelter:", shelter_animals)
