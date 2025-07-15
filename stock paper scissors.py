import random

options = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your Move = Rock, Paper, Scissor: ")
comp_choice = random.choice(options)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Match Tie")
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Computer Wins :)")
    else:
        print("You Win :)")
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Computer Wins :)")
    else:
        print("You Win :)")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Computer Wins :)")
    else:
        print("You Win :)")
else:
    print("Invalid input! Please choose Rock, Paper, or Scissor.")
