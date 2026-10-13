import random

#welcome player and get number of rounds they want to play
print("Welcome to the Rock Paper Scissors game!")
rounds_desired = int(input("How many rounds would you like to play: "))

#validate that the number of rounds is odd
while rounds_desired % 2 == 0 or rounds_desired < 1:
        rounds_desired = int(input("You can only play an odd number of rounds, please enter an odd whole number: "))

#function to get and validate player_choice
def get_player_choice():
        player_choice = input("Please enter rock, paper, or scissors: ")
        player_choice = player_choice.lower()
        while player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
                player_choice = input("Please enter a valid input: rock, paper, or scissors: ").lower()
        return player_choice

#function to get randomly generated computer choice
def get_computer_choice():
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)
        return computer_choice

computer_wins = 0
player_wins = 0
#function to determine winner
def determine_winner(computer_choice, player_choice):
        if (player_choice == "rock" and computer_choice == "rock") or \
                (player_choice == "paper" and computer_choice == "paper") or \
                (player_choice == "scissors" and computer_choice == "scissors")    :
                return "tie"

        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
                return "win"
        else:
                return "loss" 


while computer_wins + player_wins < rounds_desired:
        player_choice = get_player_choice()  
        computer_choice =  get_computer_choice()   
        result = determine_winner(computer_choice, player_choice)
        
        if result == "tie":
                print(f"The computer chose {computer_choice}.")
                print("Tie! Play again.")
        elif result == "win":
                player_wins += 1
                print(f"The computer chose {computer_choice}.")
                print("You won!")
        elif result == "loss":
                computer_wins += 1
                print(f"The computer chose {computer_choice}.")
                print("You Lost!")

if computer_wins + player_wins == rounds_desired:
        if player_wins > computer_wins:
                print("-------------------------------------------")
                print(f"Score — You: {player_wins} | Computer: {computer_wins}")
                print("You win!!!")
                print("Thanks for playing!")
        if computer_wins > player_wins:
                print("-------------------------------------------")
                print(f"Score — You: {player_wins} | Computer: {computer_wins}")
                print("You lost!!!")
                print("Thanks for playing!")












                           
