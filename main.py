
# random
 # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
#show you two useful functions for no
from random import randint
from random import shuffle
from random import choice
print("random")
dice1 = randint(1,7)
print(f"Dice : {dice1}")
dice2 = randint(1,7)
print(f"Dice : {dice2}")
rolledDoubles = dice1 == dice2
if dice1 and dice2 == 1:
  print("You have horrendous luck.")
else:print("Guess your luck ain't that bad.")
if rolledDoubles:
  print("You rolled doubles.")
else: print("These are not doubles")

#practice with shuffle
my_list = range(1,51)
print(list(my_list))
my_list = list(my_list)

shuffle(my_list)
print(my_list)

my_list = randint(1,10000000000000000000000000000000000000000000000000000001)
print(my_list)

if my_list %2 == 0:
  print("Number is even")
else:print("This number is odd")

color = ["red","blue","violet","pink","black"]
random_color = choice(color)
print(f"color is {random_color}")
