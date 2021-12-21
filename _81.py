import string

input('User: ')
while True:
    password = input('Password: ')
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

    if not flag1:
        print('Password must contain numbers')
    elif not flag2:
        print('Password must contain at least 1 uppercase letter')
    elif not flag3:
        print('Password must be at least 5 digits long')
    else:
        user_password = password
        print('password is fine')
        break
