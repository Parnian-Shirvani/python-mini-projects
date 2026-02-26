# Rock Paper Scissors

import random

# round's number
rounds = int(input("How many rounds will you play? "))

total_comp = 0
total_player = 0 

for round_number in range(1 , rounds + 1) :
    
    # computer's turn
    randomNumber = random.randint(0 , 2)
    if randomNumber == 0 :
        computerMove = "rock"
    elif randomNumber == 1 :
        computerMove = "paper"
    elif randomNumber == 2 :
        computerMove = "scissors"

    # player's turn
    print("rock , paper , scissors")
    player = input("Make your move player: ")
    player = player.lower()
    
    while player not in ["rock", "paper", "scissors"] :
        player = input("Invalid input! Choose rock, paper, or scissors: ").lower()

    # game
    if player == computerMove :
        print(f"computer move is {computerMove}")
        print("Tie , Again")
    elif player == "rock" :
        if computerMove == "paper" :
            print(f"computer move is {computerMove} , you lose this round!")
            total_comp += 1
        elif computerMove == "scissors" :
            print(f"computer move is {computerMove} , you win this round!")
            total_player += 1
    elif player == "paper" :
        if computerMove == "rock" :
            print(f"computer move is {computerMove} , you win this round!")
            total_player += 1
        elif computerMove == "scissors" :
            print(f"computer move is {computerMove} , you lose this round!")
            total_comp += 1 
    elif player == "scissors" :
        if computerMove == "paper" :
            print(f"computer move is {computerMove} , you win this round!")
            total_player += 1
        elif computerMove == "rock" :
            print(f"computer move is {computerMove} , you lose this round!")
            total_comp += 1
    print("_____________________________")

# result :
if total_comp == total_player :
    print(f"Tie , player = {total_player} : {total_comp} = computer ")
elif total_comp < total_player :
    print(f"Winner , player = {total_player} : {total_comp} = computer ")
elif total_comp > total_player :
    print(f"Loser , player = {total_player} : {total_comp} = computer ")