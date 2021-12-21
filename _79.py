import string


password = input('password: ')
flag1 = False
flag2 = False
flag3 = False

for char in password:
    if char in string.digits:
        flag1 = True
    elif char in string.ascii_uppercase:
        flag2 = True
if len(password) >= 5:
    flag3 = True

if False in [flag1, flag2, flag3]:
    print('Password is not fine')
else:
    user_password = password
    print('password is fine')
