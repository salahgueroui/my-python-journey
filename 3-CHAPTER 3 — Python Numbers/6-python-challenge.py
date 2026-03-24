# Challenge 6: Python Challenge
# Generate a random integer between 1 and 100,
# then check whether it is even.

import random

print(random.randint(1,100))
if random.randint(1,100)%2==0:
    print("Even")
else:
    print("Odd")


    