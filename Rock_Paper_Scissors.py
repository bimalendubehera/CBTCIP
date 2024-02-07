import random
choices = ["Rock", "Scissors", "Paper"]

while True:
    computer_score = 0
    user_score = 0

    user_input = int(input("\nWould you like to start the game?\n1. YES\n2. NO\n"))

    if user_input == 1:
        for i in range(1, 6):
            user_choice_input = int(input("\nSelect one option:\n1. Rock\n2. Scissors\n3. Paper\n"))
            
            if user_choice_input == 1:
                user_choice = "Rock"
            elif user_choice_input == 2:
                user_choice = "Scissors"
            elif user_choice_input == 3:
                user_choice = "Paper"
            else:
                print("\nNot a valid option")
                continue

            computer_choice = random.choice(choices)

            print("Computer chose:", computer_choice)
            print("You chose:", user_choice)

            if user_choice == computer_choice:
                print("It's a draw!")
            elif (user_choice == "Rock" and computer_choice == "Scissors") or \
                 (user_choice == "Scissors" and computer_choice == "Paper") or \
                 (user_choice == "Paper" and computer_choice == "Rock"):
                print("You win this round!")
                user_score += 1
            else:
                print("Computer wins this round!")
                computer_score += 1

        print("\nFinal Scores:")
        print("Your Score:", user_score)
        print("Computer Score:", computer_score)

        if user_score == computer_score:
            print("The game is a draw!")
        elif user_score > computer_score:
            print("You win the game!")
        else:
            print("Computer win the game!")

    else:
        break
