import string


letters = []
check = 'python'

for i in range(26):
    with open('{}.txt'.format(string.ascii_lowercase[i]), 'r') as file:
        letter = file.read()
        if letter in check:
            letters.append(letter)

print(letters)
