print("Welcome to the grill!")
user_name = input("Please enter name: ")

# Pricing Constants
taco_price = 4.5  # the prices
Tortilla_price = 5.0
# Let's make this the sauce/extra cost

# Menu Options
tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]
meal_styles = ["Meat", "Veggie"]


def get_choice(options, prompt):
    print(f"\n--- {prompt} ---")
    for i, option in enumerate(options, 1):
        print(f"{i}: {option}")

    while True:
        choice = input("Select a number: ")
        if choice.isdigit():
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return options[idx]
        print(f"Invalid input. Please pick 1-{len(options)}.")


# 1. Get order details first
put = get_choice(meal_styles, "Choose Style")
choose = get_choice(filling_types, "Choose Filling")
add = get_choice(tortilla_types, "Choose Tortilla")
choice = get_choice(toppings, "Choose Topping")

# 2. Get quantity
while True:
    num_input = input("\nHow many meals do you want? ")
    if num_input.isdigit() and int(num_input) > 0:
        num_meals = int(num_input)
        break
    print("Please enter a valid number.")

# 3. Calculate Total
# Base price * quantity + (sauce fee * quantity)
total_cost = (taco_price * num_meals) + (Tortilla_price * num_meals)

# 4. Order Summary
print("\n" + "=" * 20)
print("ORDER SUMMARY")
print("=" * 20)
print(f"Customer:    {user_name}")
print(f"Style:       {put}")
print(f"Details:     {choose} on {add} with {choice}")
print(f"Quantity:    {num_meals}")
print(f"Total Cost:  ${total_cost:.2f}")
print("=" * 20)
