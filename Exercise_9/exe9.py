def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())
print('==================================================')

def get_odds():
    for x in range(10):
        if x % 2 == 1:
            print(x)

#get_odds()

def my_range(first=1, last=10, step=2):
    number = first
    while number < last:
        yield number
        number += step

ranger = my_range()
count = 0
for x in ranger:
    count += 1
    if count == 3:
        print(x)
#Определите функцию генератора get_odds(), которая возвращает нечетные
#числа из диапазона range(10). Используйте цикл for, чтобы найти и вывести
#третье возвращенное значение.
print('==================================================')

def test(funct):
    def start():
        print('start')
        funct()
    return start

@test
def foo():
    print('end')

foo()
#object = test(object)


#. Определите декоратор test, который выводит строку 'start'
# при вызове функции и строку 'end', когда функция
# завершает свою работу
print('==================================================')

class OopsException(Exception):
    pass
try:
    raise OopsException('Caught an oops')
except OopsException as exc:
    print(exc)

#Определите исключение OopsException. Сгенерируйте его и посмотрите, что
#произойдет. Затем напишите код, позволяющий поймать
# это исключение и вывести строку 'Caught an oops'.

def knights2(saying):
    def inner2():
        return "We are the knights who say: '%s'" % saying
    return inner2

a = knights2('cat')
print(a())


