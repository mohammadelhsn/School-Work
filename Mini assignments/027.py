#############################################################################
#Author: Mohammad El-Hassan
#Description: This is a header
#Date Created: 2021/09/30
#Date Modified: 2021/09/30
#############################################################################

# Imports

from random import randint

# Constants

password = input("Enter a password ")

correct_pass = "python123"

if (password == correct_pass):
    print("Password is correct!")
else: 
    print(f"Password is incorrect. The correct password was {correct_pass}")

ranNum = randint(1, 5)
guess = int(input("Enter a number between 1 and 5 "))

if (guess == ranNum):
    print(f"You guessed it, the num was {ranNum}")
else: 
    print(f"You didn't guess it, the correct num is {ranNum}")