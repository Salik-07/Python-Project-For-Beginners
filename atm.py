class ATM:
  def __init__(self):
    self.balance = 0

  def check_balance(self):
    return self.balance

  def deposit(self, amount):
    if amount <= 0:
      raise ValueError("Deposit amount must be positive.")

    self.balance += amount

  def withdraw(self, amount):
    if amount <= 0:
      raise ValueError("Withdrawal amount must be positive.")

    if amount > self.balance:
      raise ValueError("Insufficient funds.")

    self.balance -= amount

class ATMController:
  def __init__(self):
    self.atm = ATM()

  def display_menu(self):
    print("\nWelcome to the ATM!")

    choices = ["1. Check Balance", "2. Deposit", "3. Withdraw", "4. Exit"]
    for choice in choices:
        print(choice)

  def get_choice(self):
    while True:
      choice = input("Please choose an option: ")
      valid_choices = ("1", "2", "3", "4")

      if choice not in valid_choices:
        print("Invalid choice. Please try again.")
        continue

      return choice

  def get_number(self, prompt):
    while True:
      try:
        number = float(input(prompt))
        return number
      except ValueError:
        print("Please enter a valid number.")

  def check_balance(self):
    balance = self.atm.check_balance()
    print(f"Your current balance is: ${balance}")

  def deposit(self):
    while True:
      try:
        amount = self.get_number("Enter the amount to deposit: ")
        self.atm.deposit(amount)
        print(f"Successfully deposited ${amount}.")
        break
      except ValueError as error:
        print(error)

  def withdraw(self):
    while True:
      try:
        amount =  self.get_number("Enter the amount to withdraw: ")
        self.atm.withdraw(amount)
        print(f"Successfully withdrew ${amount}.")
        break
      except ValueError as error:
        print(error)

  def run(self):
    while True:
      self.display_menu()
      choice = self.get_choice()

      if choice == "1":
        self.check_balance()
      elif choice == "2":
        self.deposit()
      elif choice == "3":
       self.withdraw()
      elif choice == "4":
        print("Thank you for using the ATM.")
        break

def main():
  atm = ATMController()
  atm.run()

if __name__ == "__main__":
  main()
