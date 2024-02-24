from os import write

rooms = open("/workspaces/Python/Room Passcode Simulator/rooms.txt", 'r')
password = open("/workspaces/Python/Room Passcode Simulator/password.txt", 'r')
roomRequest = int(input("Welcome to SJCS Rooms! Please input your room number: "))

lines = rooms.readlines()
getText = password.readlines()


i = 0
while i <= len(lines):
  if roomRequest == i:
    userPasscodeInput = input("What is the passcode? ")
    
    userPasscode = getText[roomRequest-1]
    if userPasscodeInput == userPasscode:
      print("Access granted")
      break
    else:
      print("Access denied")
      break
  elif roomRequest in ["exit", "leave", "quit"]:
    break
  else:
    i += 1
    continue

if roomRequest > int(lines[-1]):
  print("This room does not exist.")
  newRoom = input("Would you like to create a new room? ")
  if newRoom.upper() == "YES":
    
    while True:
      createPassword = input("Create a new passcode (must be longer than 4 characters): ")

      if createPassword in ["password123", "password", "passcode", "123456789", "1234"]:
        print("That passcode is too weak! Please try again.")
        continue
      elif len(createPassword) < 5:
        print("Your password is too short. Please try again.")
        continue
      else:
        break

    with open("/workspaces/Python/Room Passcode Simulator/rooms.txt", 'a') as file:
      file.write("\n")
      file.write(str(len(lines) + 1))
      file.close()

    with open("/workspaces/Python/Room Passcode Simulator/password.txt", 'a') as file:
      file.write("\n")
      file.write(createPassword)

    print("You new room number is", str(len(lines)))
    print("Your passcode is", createPassword)
    print("Do not share your password with anyone and have a great stay!")
  elif newRoom.upper() == "NO":
    pass