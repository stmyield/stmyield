from random import randint

choices = ["Rock", "Paper", "Scissors"]

computer = choices[randint(0, 2)]

player = False


while player == False:
    player = input("Rock, Paper, Scissors?: ").lower()
    if player == computer:
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("You lose!", computer, "covers", player)
        else:
            print("You win!", player, "smashes", computer)
    
    elif player == "paper":
        if computer == "scissors":
            print("You lose!", computer, "cut", player)
        else:
            print("You win!", player, "covers", computer)

    elif player == "scissors":
        if computer == "rock":
            print("You lose...", computer, "smashes", player)
        else:
            print("You win!", player, "cut", computer)
    
    else:
        print("That's not a valid play. Check your spelling!")

    player = False
    computer = choices[randint(0, 2)]

    
