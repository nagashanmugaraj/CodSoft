import random

def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    print("Welcome to Rock-Paper-Scissors Game!")
    print("Choose 'rock', 'paper', or 'scissors' to play.")
    
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Your score: {user_score} | Computer score: {computer_score}")
        
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thank you for playing! Final score:")
            print(f"Your score: {user_score} | Computer score: {computer_score}")
            break

if __name__ == "__main__":
    play_game()
