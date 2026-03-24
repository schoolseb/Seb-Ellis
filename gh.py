name = input("Please enter name: ")
taco_price = 4.5
flour_price = 5.0

meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()
meal_price = flour_price if meal_choice == "flour" else taco_price
if meal_choice not in ["taco", "flour"]:
    meal_choice = "taco"

num_meals = int(input(f"How many {meal_choice}s? "))

options = {
    "Topping": ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"],
    "Filling": ["Beans", "Chicken", "Fish", "Beef"],
    "Tortilla": ["Corn", "Flour", "Whole Wheat"],
    "Type": ["Meat", "Veggie"]
}

order = {}
for category, items in options.items():
    print(f"\n--- {category} Options ---")
    for i, item in enumerate(items, 1):
        print(f"{i}: {item}")

    while True:
        res = input(f"Choose a {category} (1-{len(items)}): ")
        if res.isdigit() and 1 <= int(res) <= len(items):
            order[category] = items[int(res) - 1]
            break
        print("Invalid choice.")

print("\n" + "=" * 20 + "\nOrder Summary:\n" + "=" * 20)
print(f"User Name: {name}")
print(f"Meal: {num_meals}x {meal_choice} ({order['Type']})")
print(f"Details: {order['Filling']} on {order['Tortilla']} with {order['Topping']}")
print(f"Total cost: ${num_meals * meal_price:.2f}")
