import random


while True:

    colours = ["Violet", "Orange", "Pink",
               "Green", "Yellow", "White", "Blue", "Red"]
    print("""Welcome to Mastermind! You have to guess what four colours are in which of the four positions.
            You will have 12 attempts before game over. 
            Good Luck.""")
    print("The colours you have to choose from are: ", colours)

    print("""We will tell you if your guess has correct colours in the right place, 
            and if you have the correct colours but not in the correct place.""")
    colours_assigned = random.sample(colours, 4)
    guesses = 0

    for i in range(12):
        while True:
            player_attempt = input(
                "Enter your guess in the format of colour1,colour2,colour3,colour4: ").split(',')
            if all(color in colours for color in player_attempt):
                break
            print("Please select a valid colour from the list provided.")

        guesses += 1

        correct_colour_incorrect_position = 0
        correct_colour_correct_position = 0

        for i in range(len(player_attempt)):
            if player_attempt[i] == colours_assigned[i]:
                correct_colour_correct_position += 1
            elif player_attempt[i] in colours_assigned:
                correct_colour_incorrect_position += 1

        print("You have guessed ", correct_colour_correct_position,
              "Correct colours in the correct position.")
        print("You have guessed ", correct_colour_incorrect_position,
              "Correct colours in the incorrect position.")

        if correct_colour_correct_position == 4:
            print("Congratulations, you have won! It only took you ",
                  guesses, "attempts!")
            retry = input('Would you like to try again? Y/N: ')
            if retry != 'y':
                break

        elif guesses == 11 and correct_colour_correct_position != 4:
            print("Game Over! The correct answer was ", colours_assigned)
            retry = input('Would you like to try again? Y/N: ')
            if retry != 'y':
                break
    break
