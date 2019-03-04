

#!/usr/bin/env python3

import random

number = random.randint(1,20)



ola = input("Hey, What's your name")

print("Hello", ola + ".",)

question = input("Would you like to play a game? [Y/N] ")



    guess = int(input("Have a guess of which number: "))
    if guess > number:
        print("Guess Lower")
        if guess < number:
            print("Guess higher")
