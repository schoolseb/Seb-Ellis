import random
numbers = list(range(11))

print(numbers)

random.shuffle(numbers)

for i in range(2):
    print(numbers.pop())

