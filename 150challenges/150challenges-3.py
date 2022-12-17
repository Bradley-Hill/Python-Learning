# Challenge 35
name = input("Please enter your name: ")
for i in range(1, 4):
    print(name)
# Challenge 36
name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
for i in range(1, (number+1)):
    print(name)
# Challenge 37
name = input("Please enter your name: ")
for i in name:
    print(i)
# Challenge 38
name = input("Please enter your name: ")
number = int(input("Please enter a number: "))
for i in range(0, number):
    for letters in name:
        print(letters)
# Challenge 39
number = int(input("Please enter a number to see its times table: "))
for i in range(1, 13):
    result = i*number
    print(i, " x ", number, " = ", result)
# Challenge 40
number = int(input("Please enter a number below 50: "))
for i in range(50, (number-1), -1):
    print(i, " your number is ", number)
# Challenge 41
name = input("Please enter your name: ")
number = int(input("Please enter your number: "))
if number < 10:
    print(name)
elif number >= 10:
    for i in range(0, 3):
        print("Too High")
# Challenge 42
total = 0
for i in range(0, 5):
    number = int(input("Please enter a number: "))
    choice = input("Would you like to include this number? y/n")
    if choice == "y":
        total = total + number
print("The total sum of the numbers you chose is: ", total)
# Challenge 43
choice = int(input("Would you like to count in 1)increasing, or 2)decreasing order?: "))
if choice == 1:
    maxNumber = int(input("Please enter a number: "))
    for i in range(1, (maxNumber+1)):
        print(i)
elif choice == 2:
    lowNumber = int(input("Please enter a number under 20: "))-1
    for i in range(20, lowNumber, -1):
        print(i)
else:
    print("I don't understand.")
# Challenge 44
attendees = int(input("How many people would you like to invite to a party?: "))
if attendees >= 10:
    print("Too many people, no party allowed.")
else:
    for i in range(0, attendees):
        names = input("Please enter the name of who you would like to invite: ")
        print(names, " has been invited.")
