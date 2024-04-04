
import os

SECRETWORD = "mclaren"
correctLetters = ''
attemptsReg = 0

while True:
    letterInput = input("Please, type one letter here: ").lower()
    attemptsReg += 1 

    if len(letterInput) > 1:
        print("You have typed more than one letter.")
        print("Please, type only one letter per once.")

    if letterInput in SECRETWORD:
        correctLetters += letterInput

    correctWord = ''
    
    for secretLetter in SECRETWORD:
        if secretLetter in correctLetters:
            correctWord += secretLetter

        else:
            correctWord += "*"

    if correctWord == SECRETWORD:
        os.system("cls")
        print("You win the game! Congratulations!")
        print("The word is: ", SECRETWORD)
        print("Attempts: ", attemptsReg)
        correctLetters = ""
        attemptsReg = 0
