import random
characters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password_length = int(input("Enter the password length : "))
password = ""

for _ in range(password_length):
    password += random.choice(characters)

print(password)