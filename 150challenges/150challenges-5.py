import random

# Challenge 52
num = random.randint(1, 100)
print(num)
# Challenge 53
fruit = random.choice(["strawberry", "papaya", "kiwi", "apple", "mango"])
print(fruit)
# Challenge 54
compChoice = random.choice(["h", "t"])
userChoice = input("Please choose h(eads) or t(ails): ")
if compChoice == userChoice:
    print("You win")
elif compChoice != userChoice:
    print("Bad luck.")
print("The computer chose ", compChoice)
# Challenge 55
num = random.randint(1, 5)
userNum = int(input("Please choose a number: "))
if userNum == num:
    print("Well done!")
else:
    if userNum < num:
        print("Your number is too small")
    elif userNum > num:
        print("Your number is too big")
    userNum = int(input("Please guess one more time: "))
    if userNum != num:
        print("You lose")
    else:
        print("Correct")
# Challenge 56
num = random.randint(1, 10)
userNum = int(input("Please choose a number between 1 - 10: "))
while userNum != num:
    print("That is not the correct number!")
    userNum = int(input("Please try and guess again, 1-10: "))
# Challenge 57
num = random.randint(1, 10)
userNum = int(input("Please choose a number between 1 - 10: "))
while userNum != num:
    print("That is not the correct number!")
    if userNum > num:
        print("Your number is too high.")
    elif userNum < num:
        print("Your number is too low.")
    userNum = int(input("Please try and guess again, 1-10: "))
# Challenge 58
score = 0
for i in range(0, 5):
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    realSolution = num1 + num2
    print(num1, "+", num2, "= ??")
    solution = int(input("Please enter the correct answer: "))
    if solution == realSolution:
        score = score + 1
print("You got ", score, "correct out of 5")
# Challenge 59
colours = ["red", "blue", "green", "pink", "terracotta"]
hiddenColour = random.choice(colours)
print(colours)
guess = input("Please guess the colour the program has selected: ")
guess = guess.lower()
while guess != hiddenColour:
    if hiddenColour == "red":
        print("I bet you won't paint the town RED.")
        guess = input("Please guess the colour the program has selected: ")
    elif hiddenColour == "blue":
        print("I guess you BLUE it!")
        guess = input("Please guess the colour the program has selected: ")
    elif hiddenColour == "green":
        print("I bet you're turning GREEN with envy.")
        guess = input("Please guess the colour the program has selected: ")
    elif hiddenColour == "pink":
        print("PINK is a terrible colour on you.")
        guess = input("Please guess the colour the program has selected: ")
    elif hiddenColour == "terracota":
        print("I think there will be a TERRACOTTA army coming to take you away soon...")
        guess = input("Please guess the colour the program has selected: ")
print("Well done!")
