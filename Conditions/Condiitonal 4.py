import random
print("\nlet's create some playdate pairs!")






goldfish = ["Bubbles","Finley","Goldie","Nemo"]

print("Welcome to the goldfish Playable Planner!")
print("Our goldfish friends are: " + ",".join(goldfish))

new_fish = input("Enter the name of a new goldfish:")
goldfish.append(new_fish)

print("Updated goldfish list: "+",".join(goldfish))

fish_to_remove = input("Enter the name of a goldfish to remove: ")
if fish_to_remove in goldfish:
    goldfish.remove(fish_to_remove)
    print(fish_to_remove + " has been removed  removed  from the list.")
else:
    print("sorry," + fish_to_remove +"is not in the list")

print("current goldfish list: " + ','.join(goldfish))

random.shuffle(goldfish)

for i in range(0, len(goldfish),2):
    if i + 1 < len(goldfish):
        print(goldfish[i] + " will have a playdate with " + goldfish[i + 1])
    else:
        print(goldfish[i] + " will have a solo play session.")



