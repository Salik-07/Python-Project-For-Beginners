import re

def check_password_strength(password):
  strength = 0
  strength_mapping = [
    "Very Weak",
    "Weak",
    "Medium",
    "Strong",
    "Very Strong"
  ]


  if len(password) >= 8:
    strength += 1
  if re.search("[a-z]", password):
    strength += 1
  if re.search("[A-Z]", password):
    strength += 1
  if re.search("[0-9]", password):
    strength += 1
  if re.search("[@#$%+=!]", password):
    strength += 1

  return strength_mapping[strength - 1]

def main():
  password = input("Enter a password: ")
  strength = check_password_strength(password)

  print(f"Password strenth: {strength}")

if __name__ == "__main__":
  main()