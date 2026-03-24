# 1. Dictionary for food stands
food_stands = {
    "Sweet Martha's": "Cookie Bucket and Milk",
    "Pronto Pups": "Classic Corn Dog on a Stick",
    "The Cheese Curd Tacos": "Deep-fried Curds in a Flour Shell"
}

food_stands["Fresh French Fries"] = "Fries"
print(food_stands["Pronto Pups"])

# 2. List of Lists for attractions (Nested Structure)
attractions = [
    ["Ye Old Mill", "Tunnel of Love"],
    ["Sky glider ", "Aerial View"],
    ["Giant Slide", "Yellow Burlap Fun"]
]
for attraction in attractions:
    print(attraction[0] + " is located " + attraction[1])
# 3. Set for activities (Unique items)
activities = {"CHS Miracle of Birth Center", "Butter Sculptures", "Talent Show"}

# --- Your original code structure ---

daily_planner = {
    "Morning": [("Breakfast", food_stands["Sweet Martha's"]), ("Ride", attractions[0][0])],
    "Afternoon": [("Lunch", food_stands["Pronto Pups"]), ("Activity", list(activities)[0])],
    "Evening": [("Dinner", food_stands["The Cheese Curd Tacos"]), ("Ride", attractions[2][0])]
}

print("\nYour Minnesota State Fair Daily Planner:")
for time, plans in daily_planner.items():
    print(time + ":")
    for plan in plans:
        print("- " + plan[0] + ": " + plan[1])

