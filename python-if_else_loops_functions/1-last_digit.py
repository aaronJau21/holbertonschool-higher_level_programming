#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_number = number % 10
text = f"Last digit of {number} is {last_number}"

if last_number > 5:
    print(f"{text} and is greater than 5")
elif last_number == 0:
    print(f"{text} and is 0")
else:
    print(f"{text} and is less than 6 and not 0")
