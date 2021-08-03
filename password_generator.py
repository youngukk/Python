#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

# passwords = ""

# for count in range(0, nr_letters + nr_symbols + nr_numbers):
#   if count < nr_letters:
#     passwords += (letters[random.randint(0, len(letters) - 1)])
#     # passwords += random.choice(letters)
#   elif count < nr_letters + nr_symbols:
#     passwords +=(numbers[random.randint(0, len(numbers) - 1)])
#     # passwords += random.choice(numbers)
#   else:
#     passwords += (symbols[random.randint(0, len(symbols) - 1)])
#     # passwords += random.choice(symbols)

# print(passwords)




#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P


char = []

for count in range(0, nr_letters + nr_symbols + nr_numbers):
  if count < nr_letters:
    # char += (letters[random.randint(0, len(letters) - 1)])
    char += random.choice(letters)
  elif count < nr_letters + nr_symbols:
    # char +=(numbers[random.randint(0, len(numbers) - 1)])
    char += random.choice(numbers)
  else:
    # char += (symbols[random.randint(0, len(symbols) - 1)])
    char += random.choice(symbols)

random.shuffle(char)
password = ""
for count1 in range(0, len(char)):
  password += char[count1]
print("Your password is : " + password)