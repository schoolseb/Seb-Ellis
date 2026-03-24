from midterm import meal_choice

User_name = input("Please enter name.")
taco_price = 4# the prices
Tortilla_price = 12
original_total = 12


# Use the actual choices from your prompt (taco/flour)
if meal_choice.lower() == "taco":
    meal_price = taco_price
elif meal_choice.lower() == "flour":
    meal_price = Tortilla_price
else:
    print("Invalid choice, defaulting to taco price.")
    meal_price = taco_price
    meal_choice = "taco"

# Get quantity AFTER deciding the price
num_meals = int(input("How many meals do you want? "))
total_cost = (meal_price * num_meals) + (0.50 * num_meals)



tortilla_types = ["corn", "Flour","Whole Wheat"]
filling_types =  ["Beans","Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]
tacos = ["Meat", "Veggie"]
# add cost of tacos and make options of tacos
def display_options(options):
    #for options in options:
       # print(f"{option_number}: {option}")
        #option_number +=1
        for i in range(len(options)):
            print(f"{i+1}: {options[i]}")



def get_choice(options):
    global idx
    while True:
        response = input("please choose an item")


        if not response.isdigit():
            print("Please enter a number")
            continue

        idx =  int(response) -1

    if 0 <= idx < len(options):
        return options[idx]  # This sends the word back to your variable
    else:
        print(f"Invalid choice. Pick 1-{len(options)}")
        return None


display_options(toppings)
display_options(filling_types)
display_options(tortilla_types)
display_options(tacos)
choice = get_choice(toppings)
choose = get_choice(filling_types)
add = get_choice(tortilla_types)
put = get_choice(tacos)
print(f"User Name: {User_name}")
print(f"Meal Style: {put} {meal_choice}")
print(f"Details: {choose} on {add} with {choice}")
print(f"Total cost: ${total_cost:.2f}")
