print("You are in front of house. You see a door and a box.")
location = "outside"
face = "north"
backpack = set()
box = {'key','book','map'}
while True:
  select = input()
  select = select.split(" ")
  command = select[0]
  if len(select)>1:
    obj = select[1]
  else:
    obj = ""

  if command=="open":
    if obj=="door":
      if location=="outside":
        location = "room1"
        face = "south"
        print("You're inside the house. There are doors at the east and west and a box accross the room.")
      elif location=="room1":
        if face=="south":
          location = "outside"
          print("You're outside the house")
        if face=="east":
          location="room3"
          face = "west"
          print("You're inside another room")
      elif location=="room3":
        if face=="west":
          location="room1"
          face = "east"
          print("You're inside the house")
    elif obj=="box":
      if location=="outside":
        print("Box opened:")
        for x in box:
          print("-" + x)
        print("(You can get the object by typing: get [objectname])")
      if location=="room1":
        print("There's a key in the box")
    else:
      print("What do you want to open?")

  elif command=="go":
    face = obj
    print("You're now facing "+obj)

  elif command=="get":
    if obj in box:
      backpack.add(obj)
      box.remove(obj)
      print("Keep " + obj + " in backpack")
    else:
      print("There's no " + obj + " in the box")
  elif command=="backpack":
    for x in backpack:
      print(x)
    
  elif command=="look":
    if location=="outside":
      print("You're in front of a house. There's a door in front of you and there's a box")
    if location=="room1":
      print("You're in a room. There are doors on your right and on your left. There's a box across the room.")
    if location=="room2":
      print("There's a book shelve and there's one book opened")
    if location=="room3":
      print("There's nothing here")
      
  elif command=="read":
    if obj=="letter":
      print("The letter only shows a short line of words. It says 'Please help' and no signature. Do you think someone in the house really needs help? The door looks slightly opened.")

  else:
    print("Your word is not understandable.")
