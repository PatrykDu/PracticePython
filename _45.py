import string

for i in range(26):
    with open('{}.txt'.format(string.ascii_lowercase[i]), 'w') as file:
        file.write(string.ascii_lowercase[i])
