from array import *
import random
import math
# Challenge 88
nums = array('i', [])
newArray = array('i', [])
for y in range(0, 5):
    newValue = int(input('Enter a number: '))
    newArray.append(newValue)
nums.extend(newArray)
nums = sorted(nums)
print(nums[::-1])
# Challenge 89
numbers = array('i', [])
for x in range(0, 5):
    newNum = random.randint(0, 1000000)
    numbers.append(newNum)
for x in numbers:
    print(x)
# Challenge 90
numbers = array('i', [])
while len(numbers) < 5:
    num = int(input('Enter a number between 10 and 20: '))
    if num >= 10 and num <= 20:
        numbers.append(num)
    else:
        print('Outside the range.')
for i in numbers:
    print(i)
# # Challenge 91
numbers = array('i', [15, 25, 35, 35, 45])
print(numbers)
userNum = int(input('Please enter one of the numbers listed in the numbers array: '))
value = numbers.count(userNum)
print('Your number appears: ', value, ' times.')
# Challenge 92
firstArray = array('i', [])
newArray = array('i', [])
for y in range(0, 3):
    newValue = int(input('Enter a number: '))
    newArray.append(newValue)
for x in range(0, 5):
    randValue = random.randint(0, 1000)
    firstArray.append(randValue)
finalArray = array('i', [])
for x in firstArray:
    finalArray.append(x)
for x in newArray:
    finalArray.append(x)
finalArray = sorted(finalArray)
for nums in finalArray:
    print(nums)
# Challenge 93
count = 0
numbers = array('i', [])
secondNumbers = array('i', [])
while count < 5:
    customerValue = int(input('Please enter a number: '))
    numbers.append(customerValue)
    count = count + 1
numbers = sorted(numbers)
print(numbers)
clientChoice = int(input('Please choose a number from the list: '))
secondNumbers.append(clientChoice)
numbers.remove(clientChoice)
print(secondNumbers)
print(numbers)
# Challenge 94
firstArray = array('i', [2, 5, 98, 6, 697])
for x in firstArray:
    print(x)
clientChoice = int(input('Please choose a number from the array: '))
tryAgain = True
while tryAgain == True:
    if clientChoice in firstArray:
        print('This in position ', firstArray.index(clientChoice))
        tryAgain = False
    else:
        print('Please select a number from the array only, please try again...')
        print(firstArray)
        clientChoice = int(input('Please choose a number from the array: '))
# Challenge 95
numbers = array('i', [])
for x in range(0, 5):
    randNum = random.randint(0, 1000)
    randNum = round(randNum, 2)
    numbers.append(randNum)
print(numbers)
userNum = int(input('Please enter a number between 2 and 5: '))
while userNum < 2 or userNum > 5:
    print('Please enter a number within the correct range.')
    userNum = int(input('Please enter a number between 2 and 5: '))
else:
    for nums in numbers:
        division = nums / userNum
        print(round(division, 2))