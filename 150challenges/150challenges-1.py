# Challenge 1
firstName = input("Please enter your First Name: ")
print("Hello", firstName)
# Challenge 2
firstName = input("Please enter your first name: ")
lastName = input("Please enter your surname: ")
print("Hello ", firstName, lastName)
# Challenge 3
print("What do you call a bear with no teeth?\nA Gummy Bear!")
# Challenge 4
numOne = int(input("Please enter a number: "))
numTwo = int(input("Please enter a number: "))
print("The sum of those numbers is: ", (numOne + numTwo))
# Challenge 5
numOne = int(input("Please enter a number: "))
numTwo = int(input("Please enter a number: "))
numThree = int(input("Please enter a number: "))
print("The answer is :", ((numOne + numTwo) * numThree))
# Challenge 6
startSlices = int(input("Please enter the total number of slices you started with: "))
takenSlices = int(input("Please enter the number of slices you have taken: "))
answer = startSlices - takenSlices
print("The number of slices you have remaining is :", answer)
print("You have", answer, "slices left.")
# Challenge 7
name = input("Please enter your name: ")
age = int(input("Please enter your age: "))
print(name, "next birthday you will be ", (age + 1))
# Challenge 8
billTotal = float(input("Please enter the total of the bill: "))
numberDiners = int(
    input("Please enter the number of people you will split the bill with: ")
)
priceEach = billTotal / numberDiners
print("The price to paid by each person is: £", priceEach)
# print(type(priceEach))

# Challenge 9
numberDays = int(input("Please enter a number of days: "))
numberHours = numberDays * 24
numberMinutes = numberHours * 60
numberSeconds = numberMinutes * 60
print(
    numberDays,
    "days can be broken down into: ",
    numberHours,
    "Hours, ",
    numberMinutes,
    "Minutes and ",
    numberSeconds,
    "seconds.",
)
# Challenge 10
weightKilos = float(input("Please enter a weight in kilograms: "))
answer = weightKilos * 2.204
print("Your weight in pounds is :", answer)
# Challenge 11
bigNum = int(input("Please enter a number greater than 100: "))
smallNum = int(input("Please enter a number less than 10: "))
answer = bigNum // smallNum
print("The smaller number goes into ", bigNum, "a total of", answer, "times.")
# Challenge 12
firstNum = int(input("Please enter a number: "))
secondNum = int(input("Please enter another number: "))
if firstNum > secondNum:
    print(secondNum, firstNum)
else:
    print(firstNum, secondNum)
