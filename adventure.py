#adventure corrie

print("Welcome to Looney's Great Adventure! Thank God you're here! My town has been ambushed by a monster that has been stealing books from the library! Looks like the monster is right behind you!")
direction = input("What direction do you want to go? (left/right) ")
if direction == "left":
    print("Looks like the monster is following us! Should we go in the cave or under the bridge? ")
    way = input("cave/bridge: ")
    if way == "cave":
        print("Oh look! Its the town wizard! **The wizard has casted a spell upon the monster, putting it in shock. Good job, you defeated the monster!")
    if way == "bridge":
        print("The monster found you! You have lost.")
if direction == "right":
    print("Looks like the monster is following us! Should we go in the house or hide behind a rock?")
    way2 = input("house/rock: ")
    if way2 == "house":
        print("Shh, don't make any noise, hes right behind the corner! **You have narrowly escaped the monster")
    if way2 == "rock":
        print("The monster found you! You have lost.")
