import string

with open('letters_three_by_three.txt', 'w') as file:
    for i in range(0, len(string.ascii_lowercase), 3):
        try:
            file.write(string.ascii_lowercase[i] + string.ascii_lowercase[i+1] + string.ascii_lowercase[i+2] + '\n')
        except IndexError:
            file.write(string.ascii_lowercase[i] + string.ascii_lowercase[i + 1] + '\n')
