# Challenge 96
simpleTable = [[2,5,8],[3,7,4],[1,6,9],[4,2,0]]
# Challenge 97
row = int(input('Please select a row: '))
column = int(input('Please select a column: '))
print((simpleTable[row][column]))
# Challenge 98
row = int(input('Please select a row to display: '))
print(simpleTable[row])
extraItem = int(input('Please enter a number to add to this row: '))
simpleTable[row].append(extraItem)
print(simpleTable[row])
# Challenge 99
row = int(input('Please select a row to display: '))
column = int(input('Please select a column: '))
print((simpleTable[row][column]))
changeChoice = input('Do you wish to alter this entry? y/n: ')
if changeChoice == 'y':
    alteration = int(input('What would you like to change the entry to?: '))
    simpleTable[row][column] = alteration
    print(simpleTable[row])
else:
    print(simpleTable[row])
# Challenge 100
dictionaryTable = {'John':{'N':3056,'S':8463,'W':2694,'E':8441},
                   'Tom':{'N':4832,'S':6782,'W':3612,'E':4737},
                   'Anne':{'N':5239,'S':4802,'W':1859,'E':5820},
                   'Fiona':{'N':3904,'S':3645,'W':2451,'E':8821},}
print(dictionaryTable)
# Challenge 101
name = (input('Please select a name to display: '))
region = (input('Please select a region to display: '))
print((dictionaryTable[name][region]))
changeChoice = input('Do you wish to alter this entry? y/n: ')
if changeChoice == 'y':
    alteration = int(input('What would you like to change the entry to?: '))
    dictionaryTable[name][region] = alteration
    print(dictionaryTable[name])
else:
    print(dictionaryTable[name])
# Challenge 102
newTable = {}
for x in range(0,4):
    name = input('Please enter a name: ')
    age = int(input('Please enter an age: '))
    shoeSize = int(input('Please enter a shoe size: '))
    newTable[name] = {'Age':age, 'Shoe Size':shoeSize}
print(newTable)
name = input('Please choose one of the names: ')
print(newTable[name])
# Challenge 103
for name in newTable:
    print((name),newTable[name]['Age'])
# Challenge 104
removal = input('Please chose a name to remove from the list: ')
del newTable[removal]
for name in newTable:
    print((name),newTable[name])