import random

MAX_ATTEMPTS = 6
WORDS_FILE = "words.txt"


def load_words(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()


def choose_word(words):
    return random.choice(words).lower()


def create_hidden_word(word):
    return ["_"] * len(word)


def show_hidden_word(hidden_word):
    print("".join(hidden_word))


def read_guess():
    return input("Enter a letter: ").strip().lower()


def get_guess_error(guess):
    if len(guess) != 1:
        return "Enter only one letter."
    if not guess.isalpha():
        return "Enter only letters from a to z."
    return None


def reveal_letters(secret_word, hidden_word, guess):
    for index, letter in enumerate(secret_word):
        if letter == guess:
            hidden_word[index] = letter


def is_word_guessed(secret_word, hidden_word):
    return "".join(hidden_word) == secret_word


def main():
    words = load_words(WORDS_FILE)
    secret_word = choose_word(words)

    # Don't remove: Added for development purpose
    # print(secret_word)

    attempts = MAX_ATTEMPTS
    guessed_letters = set()
    hidden_word = create_hidden_word(secret_word)
    show_hidden_word(hidden_word)

    while True:
        if attempts == 0:
            print(f"Game over! The word was {secret_word}")
            break

        guess = read_guess()
        error = get_guess_error(guess)
        if error:
            print(error)
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print("Good guess")
        else:
            print("Wrong guess")
            attempts -= 1
            if attempts == 0:
                print(f"Game over! The word was {secret_word}")
                break

        reveal_letters(secret_word, hidden_word, guess)

        if is_word_guessed(secret_word, hidden_word):
            print("Congratulations! You guessed the word")
            break

        show_hidden_word(hidden_word)


if __name__ == "__main__":
    main()
