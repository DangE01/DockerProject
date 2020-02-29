#!/usr/bin/env python
import random
min = 1
max = 6

roll_again = "yes"
print ("We are rolling dices until we get snake eyes, or 1 , 1")
while roll_again == "yes" or roll_again == "y":
    print ("Rolling the dices...")
    print ("The values are....")
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    print ("----- -----\n"
           "|",dice1, "| |",dice2,"|\n"
           "----- -----")
    if dice1 == 1 and dice2 == 1:
        print ("Game over")
        break