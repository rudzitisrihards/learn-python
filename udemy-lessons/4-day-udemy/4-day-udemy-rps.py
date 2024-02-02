import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("\nRock, paper & scissors!")
userinput = int(input("What do you choose? Type 1 for rock, 2 for paper, 3 for scissors: "))

if userinput == 1:
    print("You chose: " + rock)
elif userinput == 2:
    print("You chose: " + paper)
elif userinput == 3:
    print("You chose: " + scissors)

computerinput = random.randint(1, 3)

if computerinput == 1:
    print("Computer chose: " + rock)
elif computerinput == 2:
    print("Computer chose: " + paper)
elif computerinput == 3:
    print("Computer chose: " + scissors)

if userinput > 3 or userinput < 1:
    print("You chose: " + str(userinput) + "! You did not input a valid number!")
elif userinput == 1 and computerinput == 3:
    print("You win!")
elif userinput == 3 and computerinput == 1:
    print("You lose!")
elif userinput == computerinput:
    print("This is a draw!")
elif computerinput > userinput:
    print("You lose!")
elif computerinput < userinput:
    print("You win!")
