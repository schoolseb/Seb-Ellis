# Seb Ellis 1/25/2026
tortilla = True
meat = "pork"
cheese = False
salsa = "mild"
guacamole = False

print("Welcome to Python's Taco Stand!")

if tortilla:
    print("Great! We have a tortilla to start our taco.")
else:
    print("Oh no! We're running out of tortillas. We can't make make a taco!")
# If chicken is true then it wll just be Chicken
if meat == "chicken":
    print("Adding some delicious chicken to your taco!")
elif meat == "beef": # Adds beef but when I add it just says vegetraian.
    print("Beef it is! Adding some juicy beef to your taco")
elif meat == "pork":
    print("Pork fan,eh? Adding pork to your taco.")
else: # add porks or not
    print("Looks like we're going vegetarian today!")

if cheese:
    print("Time for some cheese!") # gets cheese if switch there is no cheese
    if salsa == "spicy":
        print("Adding extra cheese to balance out the spicy salsa!")
    else:
        print("Adding a normal amount of cheese.")
else:
    print("No cheese on this taco.")
