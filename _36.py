def word_counter(file):

    with open(file, 'r') as file:
        string = file.read()
    return len(string.split(' '))


print(word_counter('words1.txt'))
