import random  # Random is a inbuilt

# import tavishi

game = [
    """
    ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""",
    """
    PAPER
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""",
    """
   SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""",
]


# ASCII ART
print(type(game))

print(game[0])  # Rock
print(game[1])  # Paper
print(game[2])  # Scissor


user = int(input("What do you choose?\n 0=Rock\n 1=Paper\n 2=Scissors\n Enter:  "))

if user >= 3 or user < 0:
    print("Invalid Choice")
else:
    computer = random.randint(0, 2)

    print("You choose: ")
    print(game[user])

    print("Computer choose: ")
    print(game[computer])
