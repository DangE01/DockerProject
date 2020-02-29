#!/usr/bin/env python
#importing libraries
import random
import time
#declaring varibles
min = 1
max = 6
count = 0
start = "yes"
#prompt user
print ("Let see how many times it takes until we get snake eyes, or 1 , 1")
print ("Ready")
print ("Set")
print ("GO!")
#start dice simulation
while start == "yes":
    print ("Rolling the dices...")
    print ("The values are....")
    dice1 = random.randint(min, max)
    dice2 = random.randint(min, max)
    print ("----- -----\n"
           "|",dice1, "| |",dice2,"|\n"
           "----- -----")
    #keeping count
    count += 1
    #When "snake-eyes" are rolled
    if dice1 == 1 and dice2 == 1:
        print ("FINALLY \nIt took us",count,"times!")
        break