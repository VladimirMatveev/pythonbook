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

start1 = ["fee", "fie", "foe"]
rhymes = [
 ("flop", " aget mop"),
 ("fope", "turn the rope"),
 ("fa", "get your ma"),
 ("fudge", "call the judge"),
 ("fat", "pet the cat"),
 ("fog", "walk the dog"),
 ("fun", "say we're done"),
 ]
start2 = "Someone better"


for elem in rhymes:
    #("flop", " aget mop")
    first = elem[0]
    second = elem[1]
    for start1_elem in start1:
        print(start1_elem.capitalize(), ' !')
    print(first.capitalize(), ' !')
    print(start2, ' ')
    print(second, '.')
    print('----------------------------------')
