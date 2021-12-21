d = dict(weather="clima", earth="terra", rain="chuva")

word = input('Enter word: ')
if word in d.keys():
    print(d[str(word)])
else:
    print("That word doesn't exist")
