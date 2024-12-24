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
     ______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

'''
scissors = '''

     ______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

'''


lists = [rock, paper, scissors]

choices = int(input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(lists[choices])

print("Computer chose:")

computer_choice = random.choice(lists)
print(computer_choice)

if (lists[choices] == computer_choice):
    print("It's a draw")

elif (choices == 0 and computer_choice == scissors) or \
     (choices == 1 and computer_choice == rock) or \
     (choices == 2 and computer_choice == paper):
    print("You win!")
else:
    print("You lose!")
