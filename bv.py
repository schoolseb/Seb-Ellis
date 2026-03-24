print("Welcome to the grill!")
User_name = input("Please enter name: ")
taco_price = 4.5
Tortilla_price = 5.0

meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()

# Match the logic to your prompt options
if meal_choice == "taco":
    meal_price = taco_price
elif meal_choice == "flour":
    meal_price = Tortilla_price
else:
    print("Invalid choice, defaulting to taco.")
    meal_price = taco_price
    meal_choice = "taco"

# Safety loop to prevent the ValueError crash
while True:
    num_input = input(f"How many {meal_choice}s? ")
    if num_input.isdigit():
        num_meals = int(num_input)
        break
    print("Please enter a valid whole number.")

# Calculate based on the chosen meal price
total_cost = meal_price * num_meals

# ... [rest of your options code remains the same] ...

# Final Summary Print (Fixed your string concatenation)
print(f"User Name: {User_name}")
print(f"Total Cost: ${total_cost:.2f}")
