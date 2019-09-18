'''
Created on Sep 17, 2019

@author: Jared R
CSC1700 section AM
This program will represent the game scissor, rock, paper.
The computer will get an input from the player, generate a random result, and compare results in accordance with the rules of the game.
'''

def main():
    import random
    computerNum = random.randint(0, 2)
    
    if computerNum == 0:
        comp = "scissor"
    elif computerNum == 1:
        comp = "rock"
    elif computerNum == 2:
        comp = "paper"
    
    playerNum = int(input("Please enter a number 0, 1, or 2: "))
    while playerNum < 0 or playerNum > 2:
        playerNum = int(input("Error, please enter a correct number: "))
    
    if playerNum == 0:
        player = "scissor"
    elif playerNum == 1:
        player = "rock"
    elif playerNum == 2:
        player = "paper"
    
    if computerNum == 0:
        if playerNum == 0:
            print(f"The computer is {comp}, you are {player}. It is a draw")
        elif playerNum == 1:
            print(f"The computer is {comp}, you are {player}. You win!")
        elif playerNum == 2:
            print(f"The computer is {comp}, you are {player}. You lose.")
    elif computerNum == 1:
        if playerNum == 0:
            print(f"The computer is {comp}, you are {player}. You lose.")
        elif playerNum == 1:
            print(f"The computer is {comp}, you are {player}. It is a draw")
        elif playerNum == 2:
            print(f"The computer is {comp}, you are {player}. You win!")
    elif computerNum == 2:
        if playerNum == 0:
            print(f"The computer is {comp}, you are {player}. You win!")
        elif playerNum == 1:
            print(f"The computer is {comp}, you are {player}. You lose.")
        elif playerNum == 2:
            print(f"The computer is {comp}, you are {player}. It is a draw.")
    
main()

            
    