import csv
# Challenge 111
def addingEntry():
    file = open('Books.csv', 'a')
    title = input('Enter the title: ')
    author = input('Enter the author: ')
    yearReleased = input('Enter the year of release: ')
    newEntry = title + ',' + author + ',' + yearReleased + '\n'
    file.write(str(newEntry))
    file.close()
    
def searchEntry():
    file = open('Books.csv', 'r')
    authorChoice = input('Which author do you wish to see the works of?: ')
    reader = csv.reader(file)
    for row in file:
        if authorChoice in str(row):
            print(row)
        else:
            print('Sorry, there are no authors by that name on the list.')
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
# Challenge 116
file = list(csv.reader(open('Books.csv')))
Booklist = []
for row in file:
    Booklist.append(row)
    
x = 0
for row in Booklist:
    display = x,Booklist[x]
    print(display)
    x = x + 1
getrid = int(input('Enter a row number to be deleted: '))
del Booklist[getrid]

x = 0
for row in Booklist:
    display = x,Booklist[x]
    print(display)
    x = x+1
alter = int(input('Enter a row number to alter: '))
x = 0
for row in Booklist[alter]:
    display = x,Booklist[alter][x]
    print(display)
    x = x+1
part = int(input('Which part of the row do you wish to change?: '))
newdata = input('What do you want to replace it with?: ')
Booklist[alter][part] = newdata
print(Booklist[alter])

file = open('Books.csv', 'w')
x=0
for row in Booklist:
    newrecord = Booklist[x][0]+',' + Booklist[x][1] + ',' + Booklist[x][2] + '\n'
    file.write(newrecord)
    x = x+1
file.close