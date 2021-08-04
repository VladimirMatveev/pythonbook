list = [3,2,1,0]
for x in range(0,4):
    print(x)


guess_me = 7
number = 1
while number < guess_me:
        print('too low')
        if number == guess_me:
            print('too low')
            break
        if number > guess_me:
            print('oops')
            break
        print(number+1, '\n--------------------')
        break


guess_me = 5
for number in range(10):
    print(number)
    if number < guess_me:
        print('too low')
    if number == guess_me:
        print('found it!')
        break
    if number > guess_me:
        print('oops')
        break