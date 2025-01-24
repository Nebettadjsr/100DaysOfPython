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
liste1 = [rock, paper, scissors]

print("Welcome to \"Rock\" \"Paper\" \"Scissors\"")
user_choice = int(input("Type 1 for \"Rock\",\nType 2 for \"Paper\",\nType 3 for \"Scissors\"\n")) -1

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number. You lose!")
else:
    print(f"Your choice was: {liste1[int(user_choice)]}")

    computer_choice = random.randint(0,2)

    print(f"Computer choose: {liste1[computer_choice]}")

    if user_choice == computer_choice:
        print("Draw")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You loose!")
        if computer_choice == 2:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 2:
            print("You loose!")
        if computer_choice == 0:
            print("You win!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You loose!")
        if computer_choice == 1:
            print("You win!")
