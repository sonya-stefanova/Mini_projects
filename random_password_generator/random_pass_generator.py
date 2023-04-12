#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to My Random Password Generator!")
num_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

random_password_list = []

for char in range(1, num_letters + 1):
  random_password_list.append(random.choice(letters))

for char in range(1, number_symbols + 1):
  random_password_list += random.choice(symbols)

for char in range(1, number_numbers + 1):
  random_password_list += random.choice(numbers)

random.shuffle(random_password_list)

print(f"Your password is: {''.join(random_password_list)}")
# password = ""
# for char in random_password_list:
#     password+=char
# print(password)




