import time
import random

def slow(t):
    for c in t:
        print(c, end="", flush=True)
        time.sleep(0.02)
    print()

def rcp():
    py = input(": ").lower()

    if py in ["rock", "r"]:
        py = 1
    elif py in ["paper", "p"]:
        py = 2
    elif py in ["scissor", "scissors", "s"]:
        py = 3
    else:
        return "ERROR"

    KAircp = random.randint(1,3)

    # Show choices
    choices = {1: "Rock", 2: "Paper", 3: "Scissor"}
    print("You:", choices[py])
    print("KAi:", choices[KAircp])

    # Decide winner
    if KAircp == py:
        return "Match tie."
    elif (KAircp == 1 and py == 3) or \
         (KAircp == 2 and py == 1) or \
         (KAircp == 3 and py == 2):
        return "KAi wins!"
    else:
        return "You win!"
