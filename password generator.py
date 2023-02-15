print("welcome to the password generator!!")

letters=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

numbers=["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"] 

symbols=["!", "@", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "{", "[", "}", "]", "|", "?", "/", "<", ">"]

import random

letter1=input("how many letters do you want in your password?")
numbers1=input("how many numbers do you want in your password?")
symbols1=input("how many symbol do you want in your password?")


password=[""]
for n in range (0, int(letter1)):
    password.append(random.choice(letters))
for n in range(0, int(numbers1)):
    password.append(random.choice(numbers))
for n in range (0, int(symbols1)):
    password.append(random.choice(symbols))


print(password)
random.shuffle(password)
print(password)

new_password=""
for text in password:
    new_password+=text

print(f"your password is {new_password}")
