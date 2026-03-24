import random

def pick_random_number(mylist):
    """
    Picks a random number from the given list.
    Raises ValueError if the list is empty.
    """
    if not mylist:
        raise ValueError("The list is empty. Cannot pick a random number.")
    return random.choice(mylist)

def remove_number(numbers, number_to_remove):
    """Removes the first occurrence of a specific number from the list."""
    mylist =  numbers.copy()
    try:
        mylist.remove(number_to_remove)
        print(f"Removed '{number_to_remove}' from the list.")

    except ValueError:
        # This handles the case where the number_to_remove is not in the list
        print(f"Error: '{number_to_remove}' not found in the list.")
    return mylist
# if __name__ == "__main__":
# Example list of numbers
numbers = [10, 20, 30, 40, 50]
print(f"Original list: {numbers}")
  # Example of using the remove_number function
numbers = remove_number(numbers, 20)
print(f"List after removing 20: {numbers}")
 # Example of removing a number not in the list
remove_number(numbers, 99)
print(f"List after trying to remove 99: {numbers}")



try:
    random_number = pick_random_number(numbers)
    print(f"\nList: {numbers}")
    print(f"Randomly selected number: {random_number}")
except ValueError as e:
    print(f'\n"Error: {e}")')

hello = "hello world"
hello = hello + "!"
print(hello)