import random

while True:
    choice=input("Roll the dice? (y/n): ").lower()
    if choice == 'y' or choice == 'Y':
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        print(f"({die1}, {die2})")
    elif choice == 'n':
        print("Thank you for playing !")
    else:
        print("Invalid Choice !!")
        break

