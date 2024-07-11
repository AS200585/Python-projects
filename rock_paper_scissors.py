import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Select Rock/Paper/Scissors or Q to quit : ")
    if user_input == "Q":
        break
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)

    computer_guess = options[random_number]
    print("Computer picked", computer_guess + ".")

    if user_input == "rock" and computer_guess == "scissors":
        print("User wins!!")
        user_wins += 1
    elif user_input == "paper" and computer_guess == "rock":
        print("User wins!!")
        user_wins += 1
    elif user_input == "scissors" and computer_guess == "paper":
        print("User wins!!")
        user_wins += 1
    else:
        print("Computer wins.")
        computer_wins += 1
        
print("Goodbye!")

