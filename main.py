#Create a function that returns the number of vowels 'a,e,i,o,u' in a word input.

entry = input('Enter a Word: ')
word = entry.lower()

print('There were: ' + str(word.count('a')) + ' instances of A in your word.')
print('There were: ' + str(word.count('e')) + ' instances of E in your word.')
print('There were: ' + str(word.count('i')) + ' instances of I in your word.')
print('There were: ' + str(word.count('o')) + ' instances of O in your word.')
print('There were: ' + str(word.count('u')) + ' instances of U in your word.')

#Write a program that will call a string-day of the week, when calling for a number

weekDays = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

query = input('Which number day of the week would you like? ')
Day = int(query)
while Day > 7:
    print('Pick a smaller number!')
    break

print(weekDays[Day])

poop = [12, 10, 32, 3, 66, 17, 42, 99, 20]
#a
for x in range(len(poop)):
    print(poop[x], sep = '\n')
#b
for x in range(len(poop)):
    print(str(poop[x]), ' : Squaring equals =', str(poop[x] * poop[x]))
#c
total = 0
for x in range(len(poop)):
    total += poop[x]
print(total)
#d
def productOflist(poop):
    result = 1
    for x in poop:
        result = result * x
    return result
print(productOflist(poop))