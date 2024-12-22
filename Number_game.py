import random

num=(random.randint(1,10))
print("GUESS THE NUMBER FROM 1 TO 10")
playing=True
while playing:
    guess=int(input("Give a number"))
    if guess==num:
        print("Your guess was correct")
        break
    else:
        print("That is wrong try again")
