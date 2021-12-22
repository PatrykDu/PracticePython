input_value = ''
with open('user_data_commas.txt', 'w') as file:
    file.write('')
while input_value != 'close':
    if input_value == 'close':
        exit()
    input_value = input("Enter values: ")
    with open('user_data_commas.txt', 'a') as file:
        file.write(str(input_value + '\n'))
