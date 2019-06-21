# Python program to Guess the number

import random

def guessnum():
    num = random.randint(1,9)
    option = int(input("Enter number (1 - 9): "))
    count = 1
    while (num!= option):
        if(option>num):
            print("Entered input is high")
            count+=1
            option = int(input("Enter number (1 - 9): "))
            continue
        elif(option < num):
            print("Entered input is low")
            count +=1
            option = int(input("Enter number (1 - 9): "))
            continue
    print("Bingo! you found it.")
    print("Number of attempts: {}".format(count))

print("Guess the Number!")
guessnum()
