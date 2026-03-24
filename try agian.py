print("Welcome to the grill!")
User_name = input("Please enter name: ")
taco_price = 4
Tortilla_price = 12

meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()

# Fixed logic: match the input options provided in the prompt
if meal_choice == "meat":
    meal_price = taco_price
elif meal_choice == "veggies":
    meal_price = Tortilla_price
else:
    meal_price = taco_price
    meal_choice = "taco"

num_meals = int(input("How many meals do you want? "))
# Corrected math: price * quantity + sauce fee
total_cost = (meal_price * num_meals) + (0.50 * num_meals)

tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]
tacos = ["Meat", "Veggie"]


def display_options(options):
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")


def get_choice(options):
    while True:
        response = input("Please choose an item number: ")

        if not response.isdigit():
            print("Please enter a valid number.")
            continue

        # Subtract 1 because lists start at 0, but display starts at 1
        idx = int(response) - 1

        if 0 <= idx < len(options):
            return options[idx]
        else:
            print(f"Please enter a number between 1 and {len(options)}.")


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
print(f"Details: {choose} on {add} with {choice}")
print(f"Total cost: ${total_cost:.2f}")
