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
