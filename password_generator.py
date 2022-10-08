#Password Generator Project
from msvcrt import getch
from ntpath import join
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password = ""

for i in range(0, nr_letters):
    l = random.randint(0, (len(letters))-1)
    p1 = (letters[l])
    password = password + p1

for j in range(0, nr_symbols):
    n = random.randint(0, (len(symbols))-1)
    p2 = (symbols[n])
    password = password + p2

for k in range(0, nr_numbers):
    s = random.randint(0, (len(numbers))-1)
    p3 = (numbers[s])
    password = password + p3


pass_list = list(password.strip(" "))
random.shuffle(pass_list)

password_final = ""

for l in range(0, (len(pass_list))):
    p = (pass_list[l])
    password_final = password_final + p

print(f"Your password is: {password_final}")    




getch()














