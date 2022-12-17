# Challenge 45
total = 0
while total <= 50:
    total = total + int(input("Please enter a number: "))
print(total)
# Challenge 46
number = 0
while number <= 5:
    number = int(input("Please enter a number: "))
print("The last number you entered was a ", number)
# Challenge 47
total = int(input("Please enter a number: "))
secondNum = int(input("Please enter another number: "))
total = total + secondNum
choice = input("Would you like to add another number? y/n  ")
while choice == "y":
    anotherNum = int(input("Please enter  number: "))
    total = total + anotherNum
    choice = input("Would you like to add another number? y/n  ")
print(total)
# Challenge 48
count = 0
again = "y"
while again == "y":
    input("Please enter the name of someone to invite: ")
    count = count + 1
    again = input("Would you like to enter another name to the invitations? y/n  ")
print("You have invited ", count, " people to the party.")
# Challenge 49
compNum = 50
count = 1
guess = int(input("Please enter a number to guess the secret number: "))
while guess != compNum:
    if guess < 50:
        print("Your guess was too small.")
    elif guess > 50:
        print("Your guess is too high.")
    count = count + 1
    guess = int(input(" Please guess again: "))
print("Well done! It took you ", count, " attempts to guess correctly.")
# Challenge 50
userNum = int(input("please enter a number between 10 and 20: "))
while userNum < 10 or userNum > 20:
    if userNum < 10:
        print("That number is too small.")
        userNum = int(input("please enter a number between 10 and 20: "))
    elif userNum > 20:
        print("That number is too big.")
        userNum = int(input("please enter a number between 10 and 20: "))
print("Thank You!")
# Challenge 51
num = 10
print("There are ", num, " green bottles hanging on the wall, ", num, "green bottles hanging on the wall and if one "
                                                                      "green bottle should accidentally fall.")
while num > 0:
    prediction = int(input("How many bottles are left?: "))
    if prediction != (num - 1):
        print("No, try again.")
    elif prediction == (num - 1):
        num = num - 1
        print("There will be ", num, "green bottles hanging on the wall, and if one green bottle should accidentally "
                                     "fall...")
print("There are no green bottles left hanging on the wall.")
