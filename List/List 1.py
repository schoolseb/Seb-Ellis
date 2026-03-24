import random
"what do you call a fish with no eyes? fsh"
jokes = ["what do you call a fish with no eyes? fsh",
         "What do you call if someone takes your cheese? nachoocheese",
         "Why did the chicken cross the road? to get by",
         "What happens when you sneeze? achoo! "]
number_of_jokes =  len(jokes)
print(f"there are {number_of_jokes}")

random.shuffle(jokes)

for i in range(3):
    print(jokes.pop())
    # joke=random.choice(jokes)
    # jokes.remove(joke)
    # print(joke)



