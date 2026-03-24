#Seb Ellis 3/2/2026 Midterm practice

"""Displays name,and define prices"""
print ("Welcome to the grill!")
User_name = input("Please enter name.")
taco_price = 4.5# the prices
Tortilla_price = 5.0



meal_choice = input("Do you want taco or  flour? "
                    "(taco/flour): ")
# Assigns price on the choice.
if meal_choice == "taco":
        meal_price = taco_price
elif meal_choice == "flour":
        meal_price = Tortilla_price
else:
        print("Invalid choice, defaulting to taco.")
        meal_price = taco_price
meal_choice = "taco"
"""Resting to taco if clicked wrong."""
while True:
    try:
        num_meals = int(input("How many? "))
        break # Exit the loop if it works.
    except ValueError:
        print("Oops! Please enter a whole number (e.g., 3).")
#Loop ensures it is a valid number.

total_cost = meal_price * num_meals
""""Calucate the prices"""

#Define the options.
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
#Function displays the options.


def get_choice(options):
    while True:
        response = input("please choose an item")
#User input.
        if not response:
            print("Can't skip")
            continue
            # Check if empty.
        if not response.isnumeric():
            print("Please enter a number")
            continue
#Says enter a number.
        int_response =  int(response) -1

        if int_response < 0  or int_response >= len(options):
            print(f"Please number a number between 1 and {len(options)}")
            break
        return options[int_response]
""""convert to subtract index,and validates the number to item in list."""""


def get_choose(options):
    while True:
        num_input = input(f"How many {meal_choice}s? ")
        if num_input.isdigit():
            num_input = int(num_input)
        else:
            print("Invalid only use numbers.")

            break
        print("Please enter a valid whole number.")

        int_response =  int(num_input) -1

        if int_response < 0  or int_response >= len(options):
            print(f"Please number a number between 1 and {len(options)}")
            break

        return options[int_response]
#This is for Quantity

print("\n --- Change order if you like. ---")
display_options(toppings)
choice = get_choice(toppings)

display_options(filling_types)
choose = get_choice(filling_types)

display_options(tortilla_types)
add = get_choice(tortilla_types)

display_options(tacos)
put = get_choice(tacos)
#This lets users interact to add their options.


#Prints choices.
print("You chose:", choice)
print("You chose:", choose)
print("You chose:", add)
print("You choose:", put)

#Prints Summary/Recite
print("\n" + "="*20)
print("\nOrder Summary:") # Sums up the order of items,
print("="*20)

#Prints name, food type,and the meal
print(f"User Name:  + {User_name}") # adds persons name
print("Meal Type: " + meal_choice + "meal") # displays the food
print("Original Price : " + str(taco_price)) # gets the meals

#Prints the total cost,details,and quantity.
print(f"Details: {choose} on {add} with {choice}")
print(f"quntity: {meal_choice} ")
print(f"Total cost: ${total_cost:.2f}")