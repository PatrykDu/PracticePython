import string


letters = []

for i in range(26):
    with open('{}.txt'.format(string.ascii_lowercase[i]), 'r') as file:
        letters.append(file.read())

print(letters)
