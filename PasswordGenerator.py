import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

### EASY PASSWORD

password = ""
for pw_char in range(0, nr_letters):
    password += random.choice(letters)
for pw_sym in range(0, nr_symbols):
    password += random.choice(symbols)
for pw_num in range(0, nr_numbers):
    password += random.choice(numbers)
print(f"Your easy Password is: {password}") # easy Password

### AddOn for HARD PASSWORD

password_rnd_list = list(password) #converst str to list
random.shuffle(password_rnd_list) #use shuffle on list
password_rnd = ''.join(password_rnd_list) #convert list sto str

print(f"Your hard Password is: {password_rnd}")  # hard Password

########### Random PW only one question

digits = int(input("How many Digits should your Password have?\n"))
new_pw_list = [letters, numbers, symbols]
new_pw = []
for pw_char in range(digits):
    char_type = random.choice(new_pw_list)
    new_pw.append(random.choice(char_type))
new_pw1 = ''.join(new_pw)
print(f"Your random Password is: {new_pw1}")

