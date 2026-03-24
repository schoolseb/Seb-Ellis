raining = False

countdown = 10
while raining:
        print("stay inside")
        countdown -= 1
        if countdown == 0:
            raining = False
print(f"raining={raining}")
print("finally we can go outside")