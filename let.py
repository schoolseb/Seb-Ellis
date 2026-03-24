print("Welcome to the grill!")
User_name = input("Please enter name: ")
taco_price = 4.5
Tortilla_price = 5.0

meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()

if meal_choice == "taco":
    meal_price = taco_price
elif meal_choice == "flour":
    meal_price = Tortilla_price
else:
    print("Invalid choice, defaulting to taco.")
    meal_price = taco_price
    meal_choice = "taco"

while True:
    try:
        num_meals = int(input("How many? "))
        break # Exit the loop if the number is valid
    except ValueError:
        print("Oops! Please enter a whole number (e.g., 3).")

total_cost = meal_price * num_meals

tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]
tacos = ["Meat", "Veggie"]


def display_options(options):
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")


def get_choice(options):
    while True:
        response = input("Please choose a number: ")
        if not response:
            print("Can't skip")
            continue
        # Added () to call the method
        if not response.isnumeric():
            print("Please enter a number")
            continue

        int_response = int(response) - 1

        if int_response < 0 or int_response >= len(options):
            print(f"Please enter a number between 1 and {len(options)}")
            continue  # Use continue so they can try again

        return options[int_response]


print("\n--- Customize your order ---")
display_options(toppings)
choice = get_choice(toppings)

display_options(filling_types)
choose = get_choice(filling_types)

display_options(tortilla_types)
add = get_choice(tortilla_types)

display_options(tacos)
put = get_choice(tacos)

print("\n" + "=" * 20)
print("Order Summary:")
print("=" * 20)

print(f"User Name: {User_name}")
print(f"Meal Type: {meal_choice}")
print(f"Details: {choose} {put} taco on {add} with {choice}")
print(f"Quantity: {num_meals}")
print(f"Total cost: ${total_cost:.2f}")
