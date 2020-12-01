print('Enter correct username and password combo to continue')
count=0
while count < 3:
    username = input('Enter username: ')
    password = input('Enter password: ')
    if password=='1122334455' and username=='hack':
        print('Access granted')
        break
    else:
        print('Access denied. Try again.')
        count += 1