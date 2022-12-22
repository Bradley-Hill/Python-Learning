import csv
import random
# Challenge 111
def addingEntry():
    '''Adds an entry to Books.csv file'''
    file = open('Books.csv', 'a')
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    yearReleased = input('Enter the year of release: ')
    newEntry = title + ',' + author + ',' + yearReleased + '\n'
    file.write(str(newEntry))
    file.close()
    
def searchEntry():
    '''Searches Books.csv file for row containing user input'''
    file = open('Books.csv', 'r')
    authorChoice = input('Which author do you wish to see the works of?: ')
    reader = csv.reader(file)
    for row in file:
        if authorChoice in str(row):
            print(row)
        else:
            print('Sorry, there are no authors by that name on the list.')
    file.close()
    
def addingQuizEntry():
    name = input('What is your name?: ')
    question1num1 = random.randint(1,100)
    question1num2 = random.randint(1,100)
    question2num1 = random.randint(1,100)
    question2num2 = random.randint(1,100)
    QuestionOne = str(question1num1) + '+' + str(question1num2) + '='
    QuestionTwo = str(question2num1) + 'x' + str(question2num2) + '='
    print(QuestionOne)
    AnswerOne = int(input('Answer to question One: '))
    RealAnswerOne = question1num1 + question1num2
    print(QuestionTwo)
    AnswerTwo = int(input('Answer to question Two: '))
    RealAnswerTwo = question2num1 * question2num2
    score = 0
    if AnswerOne == RealAnswerOne:
        score = score + 1
    if AnswerTwo == RealAnswerTwo:
        score = score + 1
    
    file = open('MathQuiz.csv', 'a')
    newrecord = name + ',' + QuestionOne + ',' + str(AnswerOne) + ',' + QuestionTwo + ',' + str(AnswerTwo) + ','+ str(score) + ',\n'
    file.write(str(newrecord))
    file.close()
         
    

# file = open('Books.csv', 'w')

# for x in range(0,4):
#     addingEntry()
## Challenge 112
# addingEntry()
## Challenge 113
# repetions = int(input('How many new entries do you wish to add to Books.csv?: '))
# for x in range(0,repetions):
#     addingEntry()
# searchEntry()
## Challenge 114
# file = open('Books.csv', 'r')
# temp = []
# reader = csv.reader(file)
# start = int(input('Please select a starting year: '))
# end = int(input('Please select an ending year: '))

# temp = list(reader)
# x = 0
# for item in temp:
#     if int(temp[x][2]) >= start and int(temp[x][2]) <= end:
#         print(temp[x])
#         x = x+1
# file.close()
## Challenge 115
# file = open('Books.csv', 'r')
# reader = csv.reader(file)
# x = 0
# for row in file:
#     print('Row ' + str(x) + ' ' + str(row))
#     x += 1
# # Challenge 116
# file = list(csv.reader(open('Books.csv')))
# Booklist = []
# for row in file:
#     Booklist.append(row)
    
# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x = x + 1
# getrid = int(input('Enter a row number to be deleted: '))
# del Booklist[getrid]

# x = 0
# for row in Booklist:
#     display = x,Booklist[x]
#     print(display)
#     x = x+1
# alter = int(input('Enter a row number to alter: '))
# x = 0
# for row in Booklist[alter]:
#     display = x,Booklist[alter][x]
#     print(display)
#     x = x+1
# part = int(input('Which part of the row do you wish to change?: '))
# newdata = input('What do you want to replace it with?: ')
# Booklist[alter][part] = newdata
# print(Booklist[alter])

# file = open('Books.csv', 'w')
# x=0
# for row in Booklist:
#     newrecord = Booklist[x][0]+',' + Booklist[x][1] + ',' + Booklist[x][2] + '\n'
#     file.write(newrecord)
#     x = x+1
# file.close
# Challenge 117
addingQuizEntry()