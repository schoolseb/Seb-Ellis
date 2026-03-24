tortilla_types = ["corn", "Flour", "Whole Wheat"]
filling_types = ["Beans", "Chicken", "Fish", "Beef"]
toppings = ["Cheese", "Lettuce", "Tomatoes", "Onions", "Salsa", "Sour Cream"]


# add cost of tacos and make options of tacos
def display_options(options):
    # for options in options:
    # print(f"{option_number}: {option}")
    # option_number +=1
    for i in range(len(options)):
        print(f"{i + 1}: {options[i]}")


def get_choice(options):
    while True:
        response = input("please choose an item")

        if not response.isnumeric:
            print("Please enter a number")
            continue

        int_response = int(response) - 1

        if int_response >= len(options) or int_response < 0:
            print(f"Please number a number between 1 and {len(options)}")
            continue
        return options[int_response]


display_options(toppings)
display_options(filling_types)
display_options(tortilla_types)
choice = get_choice(toppings)
choose = get_choice(filling_types)
choosing = get_choice(tortilla_types)
print(choice)
print(choose)
print(choosing)