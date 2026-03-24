#Seb Ellis Midterm 3/17/2026
# I reused a lot of code from lab 3, 5. WW.schools helped me created most codes in the last 2 weeks.
#Asks users to give their name
print ("Welcome to burgers and fries!")
User_name = input("Please add a name (fries are automatic for this code).")

#This shows the Burger parts and cost.
burger_toppings = ["Turkey Bacon",  "Onions","Chicken"]
burger_names = ["Cheese","Ham","Vegan"]
burger_toppings_price = 2.50
burger_cost = 5.00

"""""
This part asks users if they want topping or not.
If typed yes it will say adding on. If no it not add on.
I had to type this twice because the def was not being read at all so i made a second without def and it worked.
"""""
def display_toppings(burger_topping):

    while True:

        burger_toppings = input("add toppings? (y/n->")
        if  burger_toppings== "y":
            print("will add that too")
            return burger_topping
        elif  burger_toppings== "n":
            print("Toppings skipped")
            break
        else: print("Only y or n works.")

# Display options asks add toppings if yes it will say coming up.
# If no it will just skip it and if typed wrong it will say type y or n.
# Returns the list after saying yes.







#This asks users to choose their foods and toppings.
def get_choice(options):
    while True:
        response = input("choose food")

        if not response:
            print("Have to pick at least one.")
            continue

        if not response.isnumeric():
            print("Enter food number")
            continue

        int_response = int(response) -1

        if int_response < 0 or int_response >= len(options):
            print(f"Enter food or number between 1- {len(options)}")
            break
        return options[int_response]
"""""
This gets the foods together and the response  is off it make you type again . 
if grader than 0 and len it will return options which is if you type it correctly.
"""""
def display_options(options):
    for i in range(len(options)):
        print(f"{i+1}: {options[i]}")
#Def display_options enforces the display with the prints.

def get_choose(options):
# Global was the only way this could run, and it suggested it in the errors tab.
# This asks to add how much you want but  if you type words it will say only do numbers.
    global burger_names
    while True:
        try:
            burger_names = int(input(f"How many? "))

            if burger_names:
                burger_names = int(burger_names)
            else:
                print("does not work")
            break
        except ValueError:
            print(" Just Whole numbers please. (e.g., 3).")

            int_response = int(burger_names)  - 1

            if int_response < 0 or int_response >= len(options):
                print(f"Only number number from 1 to {len(options)}")
                break
            return options[int_response]



# Ths displays everything after you order.  len options references the names. I got this code from earlier codes in past couple months.
print("\n --- Custom order ---")
display_options(burger_names)
display_options(burger_toppings)

print("\n --- Add or drop toppings---")
choice = get_choice(burger_names)
choose = get_choice(burger_toppings)


total_cost = burger_cost * burger_toppings_price
#original_total = str(burger_toppings) * len (burger_names)


""""
This calculates the costings. 
I got an error the first time and it says got str instead, it needed a support index 
I looked at the code from weeks ago and other codes like this that I did. 
I tried str and it worked for only one, the other was still crashing and 
I looked up str siblings and what came up was len returns the length  (burger_names is a list)  and tried that.
"""""

print("you choose:", choice)
print("you choose:", choose)


print("\n" + "="*80)
print("\nOrder Summary:")
print("="*100)

#prints out summary  and adds a tax and says what you choose. I added a little multiplying.

print(f"username: + {User_name}") # The burger types can't  mix str or len because it will crash.
#So it told me both has to be one or the other. Str shows the list of all types pre buy.
# Len is not allowed for that so only str works on both.
print("burger type:" + choice + "burger")
# The list of costings but I only have two cost to make it not as tricky as of now.

print(f" Burger Details:{choose} on {choice}")

print("Original Total: $" +"{:.2f}".format (burger_cost))



print("Total cost: $:" + "{:.2f}".format(total_cost))

print("Topping:",  ("y" if display_toppings(burger_toppings) else "n")) # gets the code asking for toppings to work.
# I found this in an old code I have done.

"""
Prints out names, all types of burgers, 
the automatic cost. 
The details of your food. 
Formats all the cost 
Lastly it tells you the final cost.
"""