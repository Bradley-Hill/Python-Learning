# Challenge 80
firstName = input('Please enter your first name: ')
print('The length of your first name is ',  + len(firstName))
lastName = input('Please enter your first name: ')
print('The length of your first name is ', + len(lastName))
fullName = firstName + ' ' + lastName
print(fullName)
print('The total length of your full name is: ', + len(fullName))
# Challenge 81
schoolSubject = input('Please enter your favourite school subject: ')
for letter in schoolSubject:
    print(letter, end='-')
# Challenge 82
poem = '''
I am continually disappointed by nudity
decently covered breasts could look like anything when revealed,
the nipples might be eyes or snake heads or flowers glowing gold,
they might be anything, but never are.
And as for the rest of it, the whole between-the-legs business,
when I was a boy, and simply wondered about women, why back then
it was the mystery of mysteries,
and now, grown up
I still think,
I wonder what she keeps hidden, down there, beneath that cloth,
imagining miracles and mysteries and dreams
conjuring secret mouths and lips that smile and sing
craving petals, tentacles and stars,
desiring the unimaginable.

The reality of nakedness
makes me mutter Jesus Christ with delight and awe as well, of course,
but still, the revelation is in its way prosaic.
Just another gentle biped with bumps and flesh and cleft and hair,
always looking just
a little bit more awkward and less interesting
than when she wore clothes. '''
print(poem)
stringSliceOne = int(input('Choose begining point: '))
stringSliceTwo = int(input('Choose end point:'))
print(poem[stringSliceOne:stringSliceTwo])
# Challenge 83
userUpper = input('Please enter a word in uppercase: ')
if userUpper.isupper():
    print('Thank you!')
else:
    print('Try Again...')
    userUpper = input('Please enter a word in uppercase: ')
# Challenge 84
postCode = input('Please enter your post code: ')
start = postCode[0:2]
print(start.upper())
# Challenge 85
name = input('Enter your name: ')
count = 0
name = name.lower()
for x in name:
    if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u':
        count = count + 1
print('Vowels = ', count)
# Challenge 86
passwordOne = input('Enter a Password: ')
passwordTwo = input('Enter it again: ')
if passwordTwo == passwordOne:
    print('Thank you.')
elif passwordOne.lower() == passwordTwo.lower():
    print('They have to be the same case.')
else:
    print('Incorrect')
# Challenge 87
word = input('Please enter a word: ')
word = word[::-1]
for x in word:
    print(x)