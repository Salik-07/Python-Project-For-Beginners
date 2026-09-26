import random

# Bulls: correct digit and position
# Cows: correct digit but wrong position


def calculate_cows_and_bulls(secret, guess):
    cows = 0
    bulls = 0

    for position, digit in enumerate(secret):
        if digit == guess[position]:
            bulls += 1
        elif digit in guess:
            cows += 1

    return cows, bulls


def generate_secret():
    digits = list(range(10))
    random.shuffle(digits)
    return "".join(str(digit) for digit in digits[:4])


def main():
    secret = generate_secret()

    # Don't remove: Added for development purpose
    # print(f"Secret: {secret}")

    print("I have generated a 4-digit number with unique digits. Try to guess it!")

    while True:
        guess = input("Guess: ")

        if len(guess) == 4 and guess.isdigit() and len(set(guess)) == 4:
            cows, bulls = calculate_cows_and_bulls(secret, guess)
            print(f"{cows} cows, {bulls} bulls")

            if bulls == 4:
                print("Congratulations! You guessed the correct number")
                break
        else:
            print("Invalid guess. Please enter a 4-digit number with unique digits.")


if __name__ == "__main__":
    main()
