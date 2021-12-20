import string

with open('Letters in File.txt', 'w') as file:
    for letter in string.ascii_lowercase:
        file.write(letter + '\n')
