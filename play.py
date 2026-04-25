import random

def play():
    choices = ["stone", "paper", "scissor"]

    player = input("Enter stone, paper, scissor: ").lower()
    computer = random.choice(choices)

    print("Computer:", computer)

    if player == computer:
        print("Tie")
    elif (player == "stone" and computer == "scissor") or \
         (player == "paper" and computer == "stone") or \
         (player == "scissor" and computer == "paper"):
        print("You Win")
    elif player in choices:
        print("You Lose")
    else:
        print("Invalid Input")