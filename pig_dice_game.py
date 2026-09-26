import random

WINNING_SCORE = 100

def display_scores(scores, turn_score):
  print(f"\nYou scored {turn_score} points this turn.")
  print(f"Current scores: Player 1: {scores[1]}, Player 2: {scores[2]}")

def add_turn_score(scores, turn_score, player):
  scores[player] += turn_score

def wants_to_roll_again():
  while True:
    choice = input("Roll again? (y/n): ").lower()

    if choice in ["y", "n"]:
      return choice == "y"

    print("Invalid choice!")

def check_winner(scores, player):
  if scores[player] >= WINNING_SCORE:
    print(f"\nPlayer {player} wins!")
    return True

  return False

def play_turn(player):
  turn_score = 0
  print(f"\nPlayer {player}'s turn")

  while True:
    roll = random.randint(1, 6)
    print(f"You rolled a {roll}")

    if roll == 1:
      return 0

    turn_score += roll

    if wants_to_roll_again():
      continue

    return turn_score

def main():
  player = 1
  scores = {1: 0, 2: 0}

  while True:
    turn_score = play_turn(player)
    add_turn_score(scores, turn_score, player)
    display_scores(scores, turn_score)

    if check_winner(scores, player):
      break

    player = 2 if player == 1 else 1

if __name__ == "__main__":
  main()
