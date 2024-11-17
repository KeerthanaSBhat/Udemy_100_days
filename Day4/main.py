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

game_images = [rock, paper, scissors]
user_choice = int(input("Select rock,paper or scissors 0,1 or 2\n"))
print(game_images[user_choice])
com_choice = random.randint(0,2)
print("Computer chose")
print(game_images[com_choice])
if user_choice>=3 or user_choice<0:
    print("Invalid ! you lost")
elif user_choice == 0 and com_choice == 2:
    print("You win!")
elif user_choice == 2 and com_choice == 0:
    print("You lost!")
elif com_choice>user_choice:
    print("You lost")
elif com_choice<user_choice:
    print("You win!")
elif com_choice==user_choice:
    print("Its a draw")