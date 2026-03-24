

print ("Welcome to the grill!")
User_name = input("Please enter name.")
taco_price = 4.5# the prices
Tortilla_price = 5.0


total_cost = 0.0
meal_choice = input("Do you want taco or  flour? "
                    "(taco/flour): ")
if meal_choice.lower() == "meat":
    meal_price = taco_price
elif meal_choice.lower() == "veggies":
    meal_price = Tortilla_price
else:

    meal_price = taco_price
    meal_choice = "taco"
def responding():
    while True:
        taco_price = int(input("price added"))

        if not taco_price:
            print("Can't skip")
            continue
        if not taco_price.isnumeric:
            print("Please enter a number")
            continue


    total_cost = meal_price + taco_price  # adds up the total for meals


    total_cost += 0.50 *taco_price # Sauce cost this
    original_total = meal_price * taco_price


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

        if not response:
            print("Can't skip")
            continue
        if not response.isnumeric:
            print("Please enter a number")
            continue

        int_response =  int(response) -1

        if int_response < 0  or int_response >= len(options):
            print(f"Please number a number between 1 and {len(options)}")
            break
        return options[int_response]
print("\n --- Change order if you like. ---")
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
