#NUMBER GUESSING GAME

import random

print("Hi! Welcome to the Number Guessing Game.\nYou have 7 chances to guess the number. Let's start!")

lower_bound = int(input("Enter a lower bound of the range : "))
upper_bound = int(input("Enter a upper bound for tht range : "))

print(f"\nYou have 7 chances to guess the number between {lower_bound} and {upper_bound}. Let's start!")

num=random.randint(lower_bound,upper_bound)
ch=7
gc=0

while gc < ch:
    gc+=1
    guess=int(input("Enter your guess : "))

    if guess==num:
        print(f"Correct! The number is {num}. You guessed it in {gc} attempts.")

    elif gc >= ch and gc != num:
        print(f"Sorry! The number was {num}. Better luck next time.")

    elif guess > num:
        print("Too high! Try a lower number. ")

    elif  guess < num:
        print("Too low! Try a higher number.")

    else:
        print("You ran out of chances..")
        break