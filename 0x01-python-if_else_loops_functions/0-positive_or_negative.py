#!/usr/bin/python3
import random
number = random.randint(-10, 10)
x = ''
if number > 0:
	x = "is positive"
elif number == 0:
	x = "is zero"
else:
	x = "is negative"
print(f"{number} {x}")
