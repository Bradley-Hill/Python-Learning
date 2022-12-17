import math
# Challenge 13
number = int(input("Please enter a number below 20: "))
if number >= 20:
    print("Too High")
else:
    print("Thank you!")
# Challenge 14
numberRange = int(input("Please enter a number in the range, 10 - 20: "))
if numberRange >= 10 and numberRange <= 20:
    print("Thank you")
else:
    print("Incorrect Answer.")
# Challenge 15
favColour = str.lower(input("What is your favourite colour? : "))
if favColour == "red":
    print("I like red too!")
else:
    print("I don't like ", favColour, ". I prefer red.")
# Challenege 16
weather = str.lower(input("Is it raining?: "))
if weather == "yes":
    windy = str.lower(input("Is it windy?: "))
    if windy == "yes":
        print("It is too windy for an umbrella.")
    else:
        print("Take an Umbrella.")
else:
    print("Enjoy your day.")
# Challenge 17
age = int(input("What is your age?: "))
if age >= 18:
    print("You can vote")
elif age == 17:
    print("You can learn to drive")
elif age == 16:
    print("You can buy a ticket for the lottery")
else:
    print("You can go trick-or-treating")
# Challenge 18
mysteryNum = int(input("Please enter a number: "))
if mysteryNum < 10:
    print("Too Low")
elif mysteryNum > 20:
    print("Too High")
else:
    print("Correct")
# Challenge 19
triplet = int(input("Please enter your choice, 1, 2, or 3: "))
if triplet == 1:
    print("Thank You")
elif triplet == 2:
    print("Well Done")
elif triplet == 3:
    print("Correct")
else:
    print("Error Message")
# Challenge 20
firstName = input("Please enter your First Name: ")
print("The number of characters in your name is: ", len(firstName))
# Challenge 21
firstName = input("Please enter your First Name: ")
familyName = input("Please enter your Family Name: ")
print(firstName, " ", familyName)
print("The number of characters in your name is: ", len(firstName) + len(familyName))
# Challenge 22
firstName = input("Please enter your First Name in lower case: ")
familyName = input("Please enter your Family Name in lower case:  ")
firstName = firstName.title()
familyName = familyName.title()
print(firstName, " ", familyName)
# Challenge 23
nurseryLine = input("Please enter the first line of a nursery rhyme: ")
print("There are ", (len(nurseryLine) +1), " characters in that line.")
startNumber = (int(input("Please enter a starting number: ")) - 1)
endNumber = (int(input("Please enter an end number: ")) - 1)
print(nurseryLine[startNumber:endNumber])
# Challenge 24
anyWord = input("Enter any word you like: ")
print(anyWord.upper())
# Challenge 25
firstName = input("Please enter your first name: ")
if len(firstName) >= 5:
    print(firstName.lower())
else:
    surname = input("Please enter your surname: ")
    combinedName = firstName + surname
    print(combinedName.upper())
# Challenge 26
pigWord = input("Please enter a word to be converted into pig-latin: ")
pigWord = pigWord.lower()
firstLetter = pigWord[0]
if firstLetter != "a" or "e" or "i" or "o" or "u":
    lengthPigWord = len(pigWord)
    trimmedPigWord = pigWord[1:lengthPigWord]
    finalWord = trimmedPigWord + firstLetter + "ay"
else:
    finalWord = pigWord + "way"
print(finalWord.lower())
# Challenge 27
decimalNumber = float(input("Please enter a number with lots of decimal places: "))
print(decimalNumber * 2)
# Challenge 28
decimalNumber = float(input("Please enter a number with lots of decimal places: "))
print(round((decimalNumber * 2),2))
# Challenge 29
number = int(input("Please enter a whole number greater than 500: "))
squareRoot = math.sqrt(number)
print("The square root is: ", round(squareRoot,2))
# Challenge 30
pie = round(math.pi,5)
print(pie)
# Challenge 31
radius = float(input("Please enter a radius: "))
print("The area of the circle is: ", (math.pi * radius**2))
# Challenge 32
radius = float(input("Please enter a radius: "))
depth = float(input("Please enter the depth: "))
area = (math.pi * radius**2)
volume = area * depth
print("The volume of the cylinder measurements provided is: ", round(volume,3))
# Challenge 33
firstNumber = int(input("Please enter a number: "))
secondNumber = int(input("Please enter a number: "))
result = firstNumber / secondNumber
remainder = firstNumber % secondNumber
print(firstNumber, " divided by ", secondNumber, " is ", result, " and ", remainder, " remaining.")
# Challenge 34
print("""
1) Square
2) Triangle
""")
choice = int(input("Enter a Number: "))
if choice == 1:
    length = int(input("Please enter the length of a side: "))
    print("The area of your square is: ", (length**2))
elif choice == 2:
    base = int(input("Enter the base length: "))
    height = int(input("Enter the height: "))
    print("The area of your triangle is: ", ((height*base)/2))
else:
    print("You haven't chosen a Square or Circle, sorry.")