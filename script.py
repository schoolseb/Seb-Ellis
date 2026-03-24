import random

def pick_random_number(numbers):
    """
    Picks a random number from the given list.
    Raises ValueError if the list is empty.
    """
    if not numbers:
        raise ValueError("The list is empty. Cannot pick a random number.")
    return random.choice(numbers)

if __name__ == "__main__":
    # Example list of numbers
    numbers = [10, 20, 30, 40, 50]
    #pick_random_number.remove(numbers)


    remove.number(numbers, 20)
    try:
        random_number = pick_random_number(numbers)
        print(f"List: {numbers}")
        print(f"Randomly selected number: {random_number}")
    except ValueError as e:
        print(f"Error: {e}")
