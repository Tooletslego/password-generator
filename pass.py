import random
import string
import time

print("Welcome to the Password Generator!")
time.sleep(1.5)

length = int(input("How long do you want your password to be? "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your generated password is:", password)