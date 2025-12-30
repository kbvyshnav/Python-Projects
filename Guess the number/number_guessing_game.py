import random

print("Hi! Welcome to the Number Guessing Game.")
print("You have 7 chances to guess the number.\n")

lower_bound = int(input("Enter a lower bound of the range: "))
upper_bound = int(input("Enter an upper bound of the range: "))

num = random.randint(lower_bound, upper_bound)
chances = 7
attempts = 0

while attempts < chances:
    attempts += 1
    guess = int(input("Enter your guess: "))

    if guess == num:
        print(f"🎉 Correct! The number is {num}. You guessed it in {attempts} attempts.")
        break

    elif guess > num:
        print("Too high! Try a lower number.")

    else:
        print("Too low! Try a higher number.")

# runs only if loop ends WITHOUT break
if attempts == chances and guess != num:
    print(f"❌ Sorry! You ran out of chances. The number was {num}.")
