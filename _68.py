d = dict(weather="clima", earth="terra", rain="chuva")

word = input('Enter word: ')
if word.lower() in d.keys():
    print(d[str(word).lower()])
else:
    print("That word doesn't exist")
