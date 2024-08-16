import random

# Print the winning rules
print('Winning rules of the game ROCK PAPER SCISSORS are:\n'
      + "Rock vs Paper -> Paper wins \n"
      + "Rock vs Scissors -> Rock wins \n"
      + "Paper vs Scissors -> Scissors wins \n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    # Take the input from the user
    choice = int(input("Enter your choice: "))

    # Validate the input
    while choice > 3 or choice < 1:
        choice = int(input('Enter a valid choice, please: '))

    # Map the choice to the corresponding name
    if choice == 1:
        choice_name = 'Rock'
    elif choice == 2:
        choice_name = 'Paper'
    else:
        choice_name = 'Scissors'

    # Print user's choice
    print(f'User choice is: {choice_name}')
    print('Now it\'s the Computer\'s turn...')

    # Computer chooses randomly
    comp_choice = random.randint(1, 3)

    # Map computer's choice to the corresponding name
    if comp_choice == 1:
        comp_choice_name = 'Rock'
    elif comp_choice == 2:
        comp_choice_name = 'Paper'
    else:
        comp_choice_name = 'Scissors'

    print(f'Computer choice is: {comp_choice_name}')
    print(f'{choice_name} vs {comp_choice_name}')

    # Check for a draw
    if choice == comp_choice:
        print("It's a draw!")
    # Check all other conditions for winning
    elif (choice == 1 and comp_choice == 3) or \
         (choice == 2 and comp_choice == 1) or \
         (choice == 3 and comp_choice == 2):
        print("<== User wins! ==>")
    else:
        print("<== Computer wins! ==>")

    # Ask the user if they want to play again
    ans = input("Do you want to play again? (Y/N): ").lower()
    if ans == 'n':
        break

# Thank the user for playing
print("Thanks for playing!")
