import random

def pick_random_number (numbers):

    # Picks random number given. Raises error value

    if not numbers:
        raise ValueError("The list is empty. Cannot pick random number. " )
    return random.choice(numbers)

if __name__ == "__main__":

    numbers = [10,20,30,40,50]

    try:
        random_number = pick_random_number(numbers)
        print(f"list: {numbers}")
    except print(f"randomly selected number: {random_number},"):
    except ValueError as e:
        print(f"Error: {e}")
