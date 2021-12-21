from datetime import datetime

year = int(str(datetime.today())[:4])
x = int(input('What is your name?'))
print('We think you were born back in {}'.format(year - x))
