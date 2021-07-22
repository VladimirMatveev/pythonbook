secret = 7
guess = 8
if guess < 7:
    print('too low')
elif guess == secret:
    print('just right')
else:
    print('too hight')

small = True
green = False

if small:
    if small:
        print('вишня')
    else:
        print('тыква')
else:
    if small:
        print('арбуз')
    else:
        print('горошек')