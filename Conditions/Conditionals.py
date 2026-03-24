customer_name =  input("Please enter your name: ") # Sebs Cafeteria
sandwich_price = 8 # the prices
platter_price = 12
meal_choice = input("Do you want a sandwich meal or  platter meal? "
                    "(sandwich/platter): ") # Price changes on what you want.
if meal_choice.lower() == "sandwich":
    meal_price = sandwich_price
elif meal_choice.lower() == "platter":
    meal_price = platter_price
else: #if wrong it would be sandwhich no platter
    print("Invalid choice. Defaulting to sandwich meal.")
    meal_choice = "sandwich"
    meal_price = sandwich_price
num_meals = int(input("How many meals do you want?"))
total_cost = meal_price * num_meals #adds up the total for meals
extra_sauce = input("Do you want extra sauce? (yes/no): ")
if extra_sauce.lower() == "yes":
    total_cost += 0.50 * num_meals # Sauce cost this
original_total = meal_price * num_meals
sauce_added = extra_sauce.lower() == "yes"

print("\nOrder Summary:") # Sums up the order of items,
print("customer Name: " + customer_name) # adds persons name
print("Meal Type: " + meal_choice + "meal") # displays the food
print("Number of Meals: " + str(num_meals)) # gets the meals
print("Extra Sauce: " + ("yes" if sauce_added else "No")) # either adds or removes
print("Original Total: $" +"{:.2f}".format(original_total)) # Finds first cost
print("Final Total: $:" + "{:.2f}".format(total_cost)) # finds the last cost
