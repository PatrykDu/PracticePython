import string

with open('letters_two_by_two.txt', 'w') as file:
    for i in range(0, len(string.ascii_lowercase), 2):
        file.write(string.ascii_lowercase[i] + string.ascii_lowercase[i+1] + '\n')
