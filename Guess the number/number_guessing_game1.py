import random

number_to_guess= random.randint(1,100)

while True:
    try:
        guess=int(input("Guess the number between 1 to 100 : "))
        
        if guess<number_to_guess:
            print("Your number is too low..Please enter a larger one !")
        elif guess>number_to_guess:
            print("Your number is too high, enter a smaller one !")
        else:
            print("Congratulations!, you guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number !!")
