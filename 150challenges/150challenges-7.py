# Challenge 69
tuple = ('UK', 'USA', 'France', 'Belgium', 'Angola')
print(tuple)
x = input('Please enter one of the countries that have been displayed: ')
print(tuple.index(x))
# Challenge 70
y = int(input('Please enter an Index number: '))
print(tuple[y])
# Challenge 71
sportsList = ['Polo', 'Cricket']
sportsList.append(input('What is your favourite sport?: '))
print(sorted(sportsList))
# Challenge 72
SchoolSubjects = ['Maths', 'Chemistry', 'Biology', 'Physics', 'Philosophy', 'French']
print(SchoolSubjects)
BadSubject = input('Which of the listed subjects do you like least?: ')
SchoolSubjects.remove(BadSubject)
print(SchoolSubjects)
# Challenge 73
FavFoods = {}
a = input('Please enter a Favourite food of yours: ')
FavFoods[1] = a
b = input('Please enter a Favourite food of yours: ')
FavFoods[2] = b
c = input('Please enter a Favourite food of yours: ')
FavFoods[3] = c
d = input('Please enter a Favourite food of yours: ')
FavFoods[4] = d
print(FavFoods)
leastFavFood = int(input('Which Food would you like to remove?(index number only): '))
del FavFoods[leastFavFood]
print(sorted(FavFoods.values()))
# Challenge 74
Colours = ['Blue', 'Pink', 'Gray', 'Indigo', 'Violet', 'Maroon', 'Orange', 'Cerulean', 'Black', 'White']
startNum = int(input('Please enter a number between 0 and 4: '))
endNum = int(input('Please enter a number between 5 and 9: '))
print(Colours[startNum:endNum])
# Challenge 75
numList = [321, 123, 999, 666]
for x in numList:
    print(x)
choice = int(input('Please choose one of the listed numbers: '))
if choice in numList:
    print(numList.index(choice))
else:
    print('That number is not in the list!')
# Challenge 76
GuestList = []
for x in range(0, 3):
    GuestList.append(input('Enter the name of someone you want to invite: '))
Continue = input('Do you wish to continue entering names? yes/no: ')
while Continue == 'yes':
    GuestList.append(input('Enter the name of someone you want to invite: '))
else:
    print(len(GuestList))
# Challenge 77
GuestList = []
for x in range(0, 3):
    GuestList.append(input('Enter the name of someone you want to invite: '))
Continue = input('Do you wish to continue entering names? yes/no: ')
while Continue == 'yes':
    GuestList.append(input('Enter the name of someone you want to invite: '))
    Continue = input('Do you wish to continue entering names? yes/no: ')
else:
    print(GuestList)
position = input('Please type one of the names from the previous list: ')
indexNum = (GuestList.index(position))
print(indexNum)
query = input('Do you still wish for that person to come to the party? yes/no : ')
if query == 'no':
    del GuestList[indexNum]
print(GuestList)
# Challenge 78
TeleShow = ['The Wire', 'Sopranos', 'Futurama', 'Community']
for x in TeleShow:
    print(x)
Show = input('Please enter a series you wish to add to the list: ')
Place = int(input('What number index do you wish to enter the series into the list: '))
TeleShow.insert(Place, Show)
print(TeleShow)
# Challenge 79
nums = []
for x in range(0,3):
    nums.append(int(input('Please enter a number: ')))
    print(nums)
    choosing = input('Do you still want the last number to stay on the list? y/n: ')
    if choosing == 'n':
        del nums[2]
print(nums)