def advanced_words_counter(file):
    with open(file, 'r') as file:
        text = file.read().replace(',', ' ')
        print(text)
        return len(text.split(' '))


print(advanced_words_counter('words2.txt'))
