import random 

player_pts = 0 
computer_pts = 0
round_number = 1
total_rounds = 5
ties = 0 
comp_answer = ["water", "fire", "earth"]

print("Welcome to my verison of rock, paper, scissors User! Avatar Style!!\n")
print("Rules go as follows...\n")
print("You have the choices of 'water', 'fire', and 'earth'.\n")
print("Where water beats fire, fire beats earth, and lastly earth beats fire\n")
print("This game is best of 5 rounds versus the computer!\n")
print("Good luck and have fun!!")

play_again = "yes"

while play_again == "yes":
    player_pts = 0
    computer_pts = 0
    round_number = 1

    while player_pts < 3 and computer_pts < 3 and round_number <= total_rounds:
        print(f"\n---Round {round_number}---")
        round_number += 1
        player_choice = input("Choose water, fire, or earth: ")
        computer_choice = random.choice(comp_answer)
        print("\nWater, fire, earth...BEND")
        print(f"You chose: {player_choice}")
        print(f"Computer chose: {computer_choice}\n")
        if player_choice == computer_choice:
            print("Its a draw! No points awarded.")
            ties += 1
        elif player_choice == "water" and computer_choice == "fire":
            print("You win this round!")
            player_pts += 1
        elif player_choice == "fire" and computer_choice == "earth":
            print("You win this round!")
            player_pts += 1
        elif player_choice == "earth" and computer_choice == "water":
            print("You win this round!")
            player_pts += 1
        else:
            print("The computer wins this round!")
            computer_pts += 1

    print(f"\nScore: You {player_pts} | Computer: {computer_pts} | Ties: {ties} ")

    if player_pts > computer_pts:
        print("\nCongratdulations! You won the game!")
    elif computer_pts > player_pts:
        print("\nThe computer won the game! Better luck next time!")
    else:
        print("\nThe game ended in a tie!")

    play_again = input("\nWould you like to play again? (yes/no): ")

print("\nAlright thanks for playing!")
