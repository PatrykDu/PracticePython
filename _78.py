import random

characters = "abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"
password = ''
for i in range(4):
    password += characters[random.randint(0, len(characters))]
print(password)
