# Challenge 105
file = open('Numbers.txt', 'w')
file.write('5\n')
file.write('34\n')
file.write('66\n')
file.write('55\n')
file.write('99\n')
file.close()
# Challenge 106
file = open('Names.txt', 'w')
file.write('Jean\n')
file.write('Rupert\n')
file.write('Cornelius\n')
file.write('James\n')
file.write('Jake\n')
file.close()
# Challenge 107
file = open('Numbers.txt','r')
print(file.read())
file.close()
# Challenge 108
file = open('Names.txt', 'a')
extra = input('Please enter an new name for the list: ')
extra += '\n'
file.write(extra)
file.close()
file = open('Names.txt', 'r')
print(file.read())
file.close()
# Challenge 109
choice = 0
print('''
      1) Create a new file
      2)Display the file
      3)Add a new item to the file
      Make a selection of 1, 2 or 3 :
      ''')
choice = int(input('Enter your selection: '))
while choice < 1 or choice > 3:
    print('Not one of the options Please try 1,2 or 3')
    choice = int(input('Enter your selection: '))
if choice == 1:
    subject = input('Please enter a school subject: ')
    subject += '\n'
    file = open('Subject.txt', 'w')
    file.write(subject)
    file.close()
elif choice == 2:
    file = open('Subject.txt', 'r')
    print(file.read())
    file.close()
elif choice == 3:
    newSubject = input('Please enter a new school subject: ')
    newSubject += '\n'
    file = open('Subject.txt', 'a')
    file.write(newSubject)
    file.close()
# Challenge 110
file = open('Names.txt','r')
print(file.read())
file.close()
selectedName = input('Please choose a name to be removed from the file: ')
selectedName += '\n'
file = open('Names.txt','r')
for row in file:
    if row != selectedName:
        file = open('names2.txt', 'a')
        newNames = row
        file.write(newNames)
        file.close()
file.close()