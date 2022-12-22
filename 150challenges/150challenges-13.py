import random
# Challenge 118
# def UserNumber():
#     number = int(input('Please enter a number higher than 0: '))
#     return number

# number = UserNumber()
    
# def NumberCount():
#     for x in range(1,number+1):
#         print(x)
        
# NumberCount()

# def askValue():
#     num = int(input('Please enter a number greater than zero: '))
#     return num
# def counting(num):
#     n = 1
#     while n <= num:
#         print(n)
#         n = n + 1
# def main():
#     num = askValue()
#     counting(num)
    
# main()
# Challenge 119
def lowTooHigh():
    low = int(input('Please enter a number: '))
    high = int(input('Please enter a higher number than your previous entry: '))
    compNum = random.randint(low,high)
    return compNum

def guessing():
    print('I am thinking of a number...')
    guess = int(input('Please enter your guess at my number: '))
    return guess

def verifyGuess(compNum,guess):
    tryAgain = True
    while tryAgain == True:
        if compNum == guess:
            print('Correct, you win!')
            tryAgain = False
        elif compNum > guess:
            guess = int(input('Too low, try again...: '))
        else:
            guess = int(input('Too High, try again...: '))


def main():
    compNum = lowTooHigh()
    guess = guessing()
    verifyGuess(compNum,guess)

main()