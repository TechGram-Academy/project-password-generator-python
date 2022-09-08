# Password Generator
import random 

symbols_length = int(input('Enter the number of symbols:'))
digits_length = int(input('Enter the number of digits:'))
letters_length = int(input('Enter the number of letters:'))


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
digits = [1,2,3,4,5,6,7,8,9,0]
symbols = ['!','@', '#', '$', '&', '*']

password_list = []

# Getting random symbols
for i in range(0, symbols_length):
    password_list.append(random.choice(symbols))

# Getting random digits
for i in range(0, digits_length):
    password_list.append(random.choice(digits))

# Getting random letters
for i in range(0, letters_length):
    password_list.append(random.choice(letters))

# print(password_list)

random.shuffle(password_list)
password = ''
# Convert list to string 
for char in password_list:
    password = password + str(char)
print(f"your password is {password}")





