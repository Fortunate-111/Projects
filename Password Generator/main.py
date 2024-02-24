import string
import random

allowed_chars = string.ascii_letters + string.digits + string.punctuation

while True:
  try:
    passwordLength = int(input("Enter password length: "))
    break
  except ValueError:
    print("Please enter a valid number")

password = "".join(
    random.choice(allowed_chars) for i in range(int(passwordLength)))
print(password)

input1 = str(input("Do you want to save this password? Y/N: "))

if input1.upper() in ["YES", "Y"]:
  with open("password.txt", "w") as f:
    f.write(password)
    print("Password saved")
elif input1.upper() == "N":
  print("Password not saved")