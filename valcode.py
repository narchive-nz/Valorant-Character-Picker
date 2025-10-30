import random

# ------------------------------------------------------------------------------
#array:
valchars = [
  "Brimstone",
  "Viper",
  "Omen",
  "Killjoy",
  "Cypher",
  "Sova",
  "Sage",
  "Phoenix",
  "Jett",
  "Reyna",
  "Raze",
  "Breach",
  "Skye",
  "Yoru",
  "Astra",
  "KAY/O",
  "Chamber",
  "Neon",
  "Fade",
  "Harbor",
  "Gekko",
  "Deadlock",
  "Iso",
  "Clove",
  "Vyse",
  "Tejo",
  "Waylay",
  "Veto"
]

# ------------------------------------------------------------------------------
#question:
def yes_no(question):
    
    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            print(random.choice(valchars), " (press enter to close)")
            input()
            break

        elif response == "no" or response == "n":
            print("kys (press enter to close)")
            input()
            break

        else:
            print("you're literally stupid i said type Y")
            print()

# ------------------------------------------------------------------------------
#ask the user
yes_no("type Y to pick a valorant character: ")





# --- made by nate ---