User_name = input("Please enter name: ")

# Prices
taco_price = 4
tortilla_price = 12
sauce_cost = 0.50

# Options
tortilla_types = ["Corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]
tacos = ["Meat", "Veggie"]

def display_options(options):
    for i in range(len(options)):
        print(f"{i+1}: {options[i]}")

def get_choice(options):
    while True:
        response = input("Please choose a number: ")
        if not response.isnumeric():
            print("Please enter a valid number.")
            continue
        int_response = int(response) - 1
        if int_response < 0 or int_response >= len(options):
            print(f"Please enter a number between 1 and {len(options)}.")
            continue
        return options[int_response]

# User Selections
meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()

if meal_choice == "taco":
    meal_price = taco_price
elif meal_choice == "flour":
    meal_price = tortilla_price
else:
    print("Invalid choice, defaulting to taco price.")
    meal_price = taco_price

num_meals = int(input("How many meals do you want? "))

# Display menus and get selections
print("\n--- Customize Your Order ---")
display_options(tacos)
put = get_choice(tacos)

display_options(tortilla_types)
add = get_choice(tortilla_types)

display_options(filling_types)
choose = get_choice(filling_types)

display_options(toppings)
choice = get_choice(toppings)

# Calculations
original_total = meal_price * num_meals
total_cost = original_total + (sauce_cost * num_meals)

# Order Summary
print("\n" + "="*20)
print("ORDER SUMMARY")
print("="*20)
print(f"User Name: {User_name}")
print(f"Meal Style: {put} {meal_choice}")
print(f"Details: {choose} on {add} with {choice}")
print(f"Quantity: {num_meals}")
print(f"Original Total: ${original_total:.2f}")
print(f"Total Cost (incl. sauce): ${total_cost:.2f}")
