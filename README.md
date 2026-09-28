# Python Projects for Beginners

A collection of small, independent command-line Python projects. Run each script on its own from the repository directory; there is no shared application or menu.

## Getting started

Install Python 3, then clone the repository and open a terminal in its directory:

```sh
git clone https://github.com/Salik-07/Python-Project-For-Beginners.git
cd Python-Project-For-Beginners
```

Most projects use only the Python standard library. Install the additional packages for the QR code, quiz, and tic-tac-toe projects:

```sh
python -m pip install "qrcode[pil]" termcolor
```

Run any project with `python <filename>`, for example:

```sh
python tic_tac_toe.py
```

On systems where Python 3 is invoked as `python3`, use `python3` in these commands. Run `word_guessing_game.py` from this directory so it can find `words.txt`.

## Projects

| Script | What it does |
| --- | --- |
| [`atm.py`](atm.py) | Simulates balance checks, deposits, and withdrawals. The balance starts at zero each time you run it. |
| [`cows_and_bulls_game.py`](cows_and_bulls_game.py) | Guess a four-digit number with unique digits; bulls have the right digit in the right position, and cows have the right digit elsewhere. |
| [`currency_converter.py`](currency_converter.py) | Converts a positive amount between USD, EUR, and CAD using rates hard-coded in the script. |
| [`dice_rolling_game.py`](dice_rolling_game.py) | Rolls two six-sided dice until you choose to stop. |
| [`number_guessing_game.py`](number_guessing_game.py) | Guess a random number from 1 to 100 using higher/lower hints. |
| [`password_generator.py`](password_generator.py) | Creates a password of a chosen length with optional uppercase letters, numbers, and symbols. |
| [`password_strength_checker.py`](password_strength_checker.py) | Labels an entered password using length and character-category checks. |
| [`pig_dice_game.py`](pig_dice_game.py) | Two players take turns rolling or banking points; rolling a 1 loses the turn's points, and the first to 100 wins. |
| [`qr_code_generator.py`](qr_code_generator.py) | Saves entered text or a URL as a QR code image at the filename you provide. Requires `qrcode[pil]`. |
| [`quiz_game.py`](quiz_game.py) | Asks three shuffled multiple-choice questions and reports your score. Requires `termcolor`. |
| [`rock_paper_scissor.py`](rock_paper_scissor.py) | Plays rock, paper, scissors against the computer until you stop. |
| [`simple_text_editor.py`](simple_text_editor.py) | Shows an existing text file or creates one, then saves the lines you enter. Type `SAVE` on its own line to finish. |
| [`slot_machine.py`](slot_machine.py) | Spins three symbols and updates a simulated balance based on your bet and matching symbols. |
| [`tic_tac_toe.py`](tic_tac_toe.py) | Two players enter row and column coordinates from 0 to 2 until someone wins or the board fills. Requires `termcolor`. |
| [`todo_list.py`](todo_list.py) | Adds, views, and removes tasks for the current session. |
| [`word_guessing_game.py`](word_guessing_game.py) | Guess letters in a word chosen from [`words.txt`](words.txt), with six incorrect guesses allowed. |

## Notes

- The currency converter uses fixed example rates; it does not fetch live exchange rates.
- The password generator uses Python's `random` module, and the strength checker uses a simple scoring rule. Neither is intended as a security tool.
- The text editor replaces the file's contents when you save. Its `SAVE` marker cannot be entered as a line of text.
- ATM balances, to-do tasks, and game state are kept in memory and are reset when their scripts exit.
