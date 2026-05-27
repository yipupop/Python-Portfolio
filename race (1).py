#INITIALIZE
finish_line = 50  #Finish Line
tortoise_pos = 0  #Starting Position
hare_pos = 0         #Starting Position
is_hare_asleep = False #Hare starts Awake
import random


print("--- The Race Begins! ---")
# The Simulation Loop
while tortoise_pos < finish_line and hare_pos < finish_line:
    # Tortoise always moves a short distance between 1 - 3 meters at random
    tort_move = random.randint(1, 3)
    # Hare has a 30% chance of falling a sleep for a turn
    sleep_num = random.randint(1,100)
    if sleep_num <= 30:
        hare_pos = hare_pos
    # If Hare is awake, it will move 1 - 10 meters at random
    hare_move = random.randint(1, 10)
    # Print the positions of the Hare and Tortoise after each round
    tortoise_pos = tortoise_pos + tort_move
    hare_pos= hare_pos + hare_move
    print(f"Tortoise: {tortoise_pos} | Hare: {hare_pos}")


# Determine the winner
if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")


