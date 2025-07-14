import random

print("Welcome to Stone Paper Scissors Game!")
print("Choose one: stone, paper, or scissors")

# Get user choice
user = input("Your choice: ").lower()

# Get computer choice
options = ["stone", "paper", "scissors"]
computer = random.choice(options)

print("Computer chose:", computer)

# Decide winner
if user == computer:
    print("It's a draw!")
elif (user == "stone" and computer == "scissors") or \
     (user == "paper" and computer == "stone") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
elif user in options:
    print("Computer wins!")
else:
    print("Invalid input. Please choose stone, paper, or scissors.")
