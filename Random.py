import math
help(math)

value = 3.424
print(math.floor(value))
print(math.ceil(value))
print(round(value))

print(math.pi)
print(math.inf)

print(math.log(math.e))

print(math.log(100,10))

print(math.sin(10))
print(math.degrees(math.pi/2))

import random
random_rs = random.randint(0,100)
print(random_rs)

# SEED
random.seed(2)
random_rs = random.randint(0,100)
print(random_rs)

# Random choice
my_list = list(range(0,20))
choice = random.choice(my_list)
print(choice)

# Random shuffle
shuffle_rs = random.shuffle(my_list)
print(shuffle_rs)
