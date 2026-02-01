import random
dice_count=int(input("How many dice do you want to roll? "))
total=0
for i in range(dice_count):
  roll: int = random.randint(1-6)
  total += roll

print("sum of the dice:",total)


