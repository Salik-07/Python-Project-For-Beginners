import random

CHERRY_SYMBOL = "c"
MELON_SYMBOL = "w"
LEMON_SYMBOL = "l"
STAR_SYMBOL = "s"
BELL_SYMBOL = "r"

SLOT_EMOJIS = {
    CHERRY_SYMBOL: "🍒",
    LEMON_SYMBOL: "🍋",
    MELON_SYMBOL: "🍉",
    STAR_SYMBOL: "⭐",
    BELL_SYMBOL: "🔔",
}
SLOT_CHOICES = tuple(SLOT_EMOJIS.keys())
TRIPLE_MATCH_MULTIPLIER = 10
PAIR_MATCH_MULTIPLIER = 2


def show_welcome_message(starting_balance):
    print("\nWelcome to the Slot Machine Game!")
    print(f"You start with a balance of ${starting_balance}")


def spin_reels():
    return tuple(random.choice(SLOT_CHOICES) for _ in range(3))


def show_reels(reels):
    reel_emojis = [SLOT_EMOJIS[reel] for reel in reels]
    print(" | ".join(reel_emojis))


def calculate_payout(reels, bet_amount):
    if reels[0] == reels[1] == reels[2]:
        return bet_amount * TRIPLE_MATCH_MULTIPLIER
    if reels[0] == reels[1] or reels[0] == reels[2] or reels[1] == reels[2]:
        return bet_amount * PAIR_MATCH_MULTIPLIER
    return 0


def show_round_result(payout):
    if payout > 0:
        print(f"You won ${payout}!")
    else:
        print("You lost!")


def play_round(balance, bet_amount):
    reels = spin_reels()
    show_reels(reels)

    payout = calculate_payout(reels, bet_amount)
    show_round_result(payout)
    return balance - bet_amount + payout


def get_bet_amount(balance):
    while True:
        try:
            bet_amount = int(input("Enter your bet amount: $"))
        except ValueError:
            print("Please enter a valid number for the bet amount.")
            continue

        if 0 < bet_amount <= balance:
            return bet_amount

        print(f"Invalid bet amount. You can bet between $1 and ${balance}.")


def wants_to_play_again():
    return input("Do you want to play again? (y/n): ").lower() == "y"


def get_starting_balance():
    while True:
        try:
            balance = int(input("Enter your starting balance: $"))

            if balance <= 0:
                print("Balance must be a positive number.")
                continue

            return balance
        except ValueError:
            print("Please enter a valid number.")


def run_game(starting_balance):
    current_balance = starting_balance

    while True:
        print(f"\nCurrent balance: ${current_balance}")
        bet_amount = get_bet_amount(current_balance)
        current_balance = play_round(current_balance, bet_amount)

        if current_balance <= 0:
            print("You are out of money! Game over.")
            break
        if not wants_to_play_again():
            break


def main():
    starting_balance = get_starting_balance()
    show_welcome_message(starting_balance)
    run_game(starting_balance)


if __name__ == "__main__":
    main()
