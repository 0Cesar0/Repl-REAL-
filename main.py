
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

# Random Practice #1
  # Implement the randint() function from the random library that allows you to obtain an integer from 1 to 10, and store that value in a variable called random_number.
number = randint(1,11)
print("That number.")
print(number)
  
# Random Practice #2
# Implement the random() function from the random library to obtain a real number between 0 and 1, and store that value in a variable called random_number.
num2 = randint(0,1)
print(num2)
print("This number.")
# Random Practice #3
# Use the random library's choice() method to get a random item from the list of names below, and store the chosen name in a variable called raffle.
# names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
names = ["Samantha", "Carrie", "Chris", "Charlotte", "Richard"]
random_name = choice(names)
print(f"They have been chosen.:{random_name}")


  
  
