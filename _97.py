def clean_file():
    with open('user_data_commas.txt', 'w') as file:
        file.write('')


def close():
    for item in memory:
        with open('user_data_commas.txt', 'a') as file:
            file.write(str(item + '\n'))
    exit()


def save():
    for item in memory:
        with open('user_data_commas.txt', 'a') as file:
            file.write(str(item + '\n'))


clean_file()
input_text = ''
memory = []

while input_text != 'CLOSE':
    input_text = input('Enter values: ')

    if input_text == 'CLOSE':
        close()
    elif input_text == 'SAVE':
        save()
        memory = []
    else:
        memory.append(input_text)
