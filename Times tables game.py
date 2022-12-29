import random
from time import *
import threading

# Variables
guess = ""
count = 3


# Welcome (underlined) and instructions
print("\n\033[4mWelcome to the multiplication game.\033[0m")
sleep(1)

print("\n\033[4mThe rules:\033[0m"
      "\n\nYou will start with 3 lives. "
      "\n\nEvery time you get a question correct you will gain a life."
      "\nEvery time you get a question wrong you will lose a life."
      "\n\nAre you up for the challenge to beat the clock and see how many lives you have? ")

# Input the duration player would like to play
sleep(5)
t = int(input("\n \nEnter the time in minutes: "))
t *= 60


def countdown():
    global t

    for x in range(t):
        t = t - 1
        sleep(1)
        if count == 0:
            print("Out of lives")
            quit()
        if t == 0:
            print("Out of time.")
            quit()



countdown_thread = threading.Thread(target=countdown)
countdown_thread.start()


# The game
while count != 0 and t != 0:
    try:
        number1 = random.randint(0, 12)
        number2 = random.randint(0, 12)
        answer = number1 * number2
        guess = int(input(f"What is {number1} x {number2} = "))
    except ValueError:
        print("Invalid number.")
        continue
    if guess == answer and count > 0:
        print("That is correct.")
        count += 1
        print(f"You have {count} lives!\n")
    elif guess != answer and count > 0:
        print(f"The answer is: {answer}")
        count -= 1
        print(f"You have {count} lives!\n")
