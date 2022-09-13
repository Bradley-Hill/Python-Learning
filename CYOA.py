while True:
    answer = input("Would you like to play? (yes/no) ")

    if answer.lower().strip() == "yes":
        answer = input("You reach a moonlit crossroads, would you like to go left or right?")
        if answer == "left":
            answer = input("You come face to face with a wild beast! Will you run away, or attack? (run/attack) ")

            if answer == "attack":
                print("Not you're smartest move, the beast savages you to death, you lose!")

            else:
                print("Well done, a wild beast is best avoided! You managed to continue on your way. ")

        elif answer == "right":
            print("The path eventually takes you past some cliffs beside the sea, you stumble and fall, drowning, your broken bones and smashed limbs make staying afloat impossible, you lose.")

        else:
            print("Interesting choice, but no, only death waited for you, you lose!")
    else:
        print("That is such a shame...")
        break