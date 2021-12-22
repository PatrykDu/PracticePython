file2 = open('countries_clean.txt', 'a')
with open('countries_raw.txt', 'r') as file1:
    for row1 in file1:
        if len(row1) > 2:
            file2.write(row1)
