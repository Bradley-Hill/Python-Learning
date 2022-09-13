from multiprocessing import shared_memory
import random

#Saying if number is odd or even
x = random.randint(0,100)
while x % 2 >= 1:
    print(x)
    print('This number is Odd')
    break
else:
    print(x)
    print('This is an even Number')
    
#Sorting a list and printing all elements less than 5

a= [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
for i in a:
    if i < 5:
        print(i)

for i in a:
    if i < 5:
        b.append(i)

print(b)

#Create a program which asks for a number and then prints a list of the divisors for this number.
number = input('Please enter a number : ')
divisors = range(1, int(number)) 
listOfDivisors = []
for i in  divisors:
    if int(number) % i == 0:
        listOfDivisors.append(i)
        
print(listOfDivisors)

#Write a program that returns a list with only the elements that are common between them both(no duplicates)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
x = []

for i in a:
    if i in b:
        x.append(i)
print(x)

randomList1 = random.sample(range(0,100), 13)
randomList2 = random.sample(range(0,100), 13)
sharedList = []

for elem in randomList1:
    if elem in randomList2:
        sharedList.append(elem)

print(sharedList)
print(randomList1)
print(randomList2)

wordList = input('Please enter a word: ')
if wordList[:1] == wordList[-1]:
    print('This word is possibly a palindrome')