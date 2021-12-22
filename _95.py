input_values = input("Enter values: ")
items = input_values.split(',')
items = [item.strip() + '\n' for item in items]
with open('user_data_commas.txt', 'w') as file:
    file.write('')
with open('user_data_commas.txt', 'a') as file:
    for item in items:
        file.write(item)
