import random
user_score = 0
computer_score = 0

while True:
    print("\nChoices: rock, paper, scissors")
    user_choice = input("Enter your choice: ").lower()
    choices = ["rock", "paper", "scissors"]

    if user_choice not in choices:
        print("Wrong,Please choose rock, paper, or scissors.")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

  
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Final Score:")
        print(f"You: {user_score} | Computer: {computer_score}")
        break
