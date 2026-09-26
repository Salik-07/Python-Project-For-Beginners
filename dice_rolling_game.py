import random

while True:
    choice = input("Roll the dice? (y/n): ").lower()
    if choice == "y":
        dice_1 = random.randint(1, 6)
        dice_2 = random.randint(1, 6)
        print(f"({dice_1}, {dice_2})")
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice!")
