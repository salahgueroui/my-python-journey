# Challenge 5: Random
# Practice using the random module (randint, random, choice, shuffle, etc.)

import random

#randint() returns a random integer between the two numbers
print(random.randint(1,10))

#random() returns a random float between 0 and 1
print(random.random())

#choice() returns a random element from a list
print(random.choice([1,2,3,4,5]))

#shuffle() shuffles a list in place
numbers = [1, 2, 3, 4, 5]
print("before:", numbers)
random.shuffle(numbers)
print("after:", numbers)