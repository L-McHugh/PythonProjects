import random
import time
import string
import secrets

# using ASCII codes
upper_letter_1 = chr(random.randint(65, 90))
upper_letter_2 = chr(random.randint(65, 90))
lower_letter_1 = chr(random.randint(97, 122))
lower_letter_2 = chr(random.randint(97, 122))
number_1 = str(chr(random.randint(48, 57)))
number_2 = str(chr(random.randint(48, 57)))
symbol_1 = secrets.choice(string.punctuation)
symbol_2 = secrets.choice(string.punctuation)


password = [upper_letter_1, upper_letter_2, lower_letter_1, lower_letter_2, number_1, number_2, symbol_1, symbol_2]
random.shuffle(password)

print("\nPassword generator"
      "\n The password created will have two uppercase letters, two lower case letters, two symbols and two numbers."
      )

time.sleep(1)

question = input("\nDo you want a random password? \n(Enter yes)")

print("\n")
if question != "Y".lower() and not "YES".lower() and not "YE".lower():
    print("O.K.")
else:
    print("".join(password))



