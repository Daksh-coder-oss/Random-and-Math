import random

while True:
    actions=["Rock","Paper","Scissors"]
    computer_action=random.choice(actions)
    user_action=input("Please enter your action")

    if user_action==computer_action:
        print("Tie")
    elif user_action=="Rock":
        if computer_action=="Scissor":
            print("You won")
        else:
            print("You lost")
    elif user_action=="Paper":
        if computer_action=="Rock":
            print("You won")
        else:
            print("You lost")
    elif user_action=="Scissor":
        if computer_action=="Paper":
            print("You won")
        else:
            print("You lost")
    play_again=input("Do you want to play againy/n?")
    if play_again=="n":
        break
    


