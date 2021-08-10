#-------------------(7.1-7.7)--------------------------#

years_list = [2000, 2001, 2002, 2003, 2004, 2005]
print(years_list[3])
print(years_list[-1])
things = ['mozzarella', 'cinderella', 'salmonella']
things[1] = 'Cindrella'
print('Пишем имя с большой: ', things)
things[0] = 'mozzarella'.upper()
print('Делаем сыр с капсом: ', things)
del things[-1]
print('Лечим болезнь: ', things)

#-------------------(7.8-7.9)--------------------------#

surprise = ['Groucho', 'Chico', 'Harpo']
surprise[-1] = surprise[-1].lower()
print(*reversed(surprise))

#--------------------(7.10)---------------------------#

even = []
for number in range(10):
    if number % 2 == 0:
        even.append(number)
print(even,'\n------------------------------------------')




#---------------------(7.11)--------------------------#
#????????????????????????????????????????????????????????
start1 = ["fee", "fie", "foe"]
rhymes = [
 ("flop", "get a mop"),
 ("fope", "turn the rope"),
 ("fa", "get your ma"),
 ("fudge", "call the judge"),
 ("fat", "pet the cat"),
 ("fog", "walk the dog"),
 ("fun", "say we're done"),
 ]
start2 = "Someone better"
first = start1
for first in first:
    first = first.capitalize()
    print(first, ' !')
#????????????????????????????????????????????????????????


#выведите на экран значение переменной first, также записав его с большой буквы и с восклицательным знаком на конце.
# Для второй строки:
#выведите на экран значение переменной start2 и пробел;
#выведите на экран значение переменной second и точку