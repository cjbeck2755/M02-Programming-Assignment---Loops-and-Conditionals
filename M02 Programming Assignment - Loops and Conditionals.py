# -*- coding: utf-8 -*-
"""
#M02 Programming Assignment - Loops and Conditionals
#C.J. Becker
#1/29/2024
#Python 3.8.10
#various textbook assignments
"""

#4.1
secret = 5
guess = 4
if(guess == secret):
    print("You got it")
elif(guess > secret):
    print("Too big")
else:
    print("Too small")

#4.2
myList = ["cherry", "pea", "watermelon", "pumpkin"]
green = 0
small = 0
for x in myList:
    if (x == "cherry" or x == "pea"):
        small = 1
    else:
        small = 0
    if (x == "watermelon" or x == "pea"):
        green = 1
    else:
        green = 0
    
    if(small):
        if(green):
            print("pea")
        else:
            print("cherry")
    elif(green):
        print("watermelon")
    else:
        print("pumpkin")

#6.1
numList = [3, 2, 1, 0]
for x in numList:
    print(x)

#6.2
guess_me = 7
number = 1
while number <= 10:
    if(number < guess_me):
        print("too low")
    elif(number == guess_me):
        print("found it!")
        break
    else:
        print("oops")
    number += 1

#6.3
guess_me = 5
for number in range(10):
    if(number < guess_me):
        print("too low")
    elif(number == guess_me):
        print("found it!")
        break
    else:
        print("oops")
