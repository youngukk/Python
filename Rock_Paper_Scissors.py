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

Your_RSP = [rock, paper, scissors]
Com_RSP = [rock, paper, scissors]

choice_num = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors : "))
if choice_num < 0 or choice_num > 2:
  print("You typed an invalid number, you lose")


com_num = random.randint(0, 2)

print(Your_RSP[choice_num])
print("Computer chose : ")
print(Com_RSP[com_num])

if choice_num == com_num:
  print("Draw")
elif choice_num == 0 and com_num == 2:
  print("You Win!")
elif choice_num < com_num :
  print("You lose")
elif choice_num == 2 and com_num == 0:
  print("You lose!")
else:
  print("You Win!")


# if choice_num == 0:
#   if com_num == choice_num:
#     print("Draw")
#   elif com_num == 1:
#     print("You Lose")
#   else:
#     print("You Win!")

# elif choice_num == 1:
#   if com_num == choice_num:
#     print("Draw")
#   elif com_num == 2:
#     print("You Lose")
#   else:
#     print("You Win!")

# else:
#   if com_num == choice_num:
#     print("Draw")
#   elif com_num == 0:
#     print("You Lose")
#   else:
#     print("You Win!")
