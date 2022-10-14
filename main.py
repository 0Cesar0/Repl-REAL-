from random import randit
# random
 # Python comes with a built in random library. There are a lot of functions included in this random library, so we will only 
#show you two useful functions for no
print("random")
dice1 = randit(1,7)
print(f"Dice : {dice1}")
dice2 = randit(1,7)
print(f"Dice : {dice2}")
rolledDoubles = dice1 == dice2
if rolledDoubles:
  print("You rolled doubles.")
else: print("These are not doubles")