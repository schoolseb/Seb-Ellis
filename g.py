

print ("Welcome to the grill!")
User_name = input("Please enter name.")
taco_price = 3# the prices
Tortilla_price = 12


meal_choice = input("Do you want taco or flour? (taco/flour): ").lower()
if meal_choice  == "meat":
    meal_price = taco_price
elif meal_choice  == "veggies":
    meal_price = Tortilla_price
else:

    meal_price = taco_price
    meal_choice = "taco"

    num_meals = int(input("How many meals do you want?"))



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
    while True:
        response = input("please choose an item")

        if not response.isdigit():
            print("Please enter a valid number.")
            continue

        # Subtract 1 because lists start at 0, but display starts at 1
        idx = int(response) - 1

        if 0 <= idx < len(options):
            return options[idx]
        else:
            print(f"Please enter a number between 1 and {len(options)}.")
print("\n --- Change order if you like. ---")
display_options(toppings)
choice = get_choice(toppings)

display_options(filling_types)
choose = get_choice(filling_types)

display_options(tortilla_types)
add = get_choice(tortilla_types)

display_options(tacos)
put = get_choice(tacos)




print("You chose:", choice)
print("You chose:", choose)
print("You chose:", add)
print("You choose:", put)
print("\n" + "="*20)
print("\nOrder Summary:") # Sums up the order of items,
print("="*20)

print(f"User Name:  + {User_name}") # adds persons name
print("Meal Type: " + meal_choice + "meal") # displays the food
print("Number of Meals: " + str(taco_price)) # gets the meals
print("price:" + "")

print(f"Details: {choose} on {add} with {choice}")
print(f"quntity: {meal_choice} ")
print(f"Total cost: ${total_cost:.2f}")