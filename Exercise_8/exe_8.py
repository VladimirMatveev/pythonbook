#-------------------8.1-8.2--------------------------#
ef2 = {
'Sobaka': ['dog','chien'],
'Kot': ['cat','chat'],
'Morj': ['walrus','morse'],
}
print(ef2)
print(ef2['Morj'][1])

#-------------------8.3-8.5--------------------------#
f2e = ef2
print(f2e.items())
print(f2e['Sobaka'][0])

print([value[0] for value in f2e.values()])
print('==================================================')

#-------------------8.6-8.9--------------------------#
anima = {
         'cats': ['Henri','Grumpy','Lucy'],
         'octopi': '',
         'emus': ''}
life = {
    'animals': anima,
    'plants' : '',
    'other' : ''
}
print(life.keys())
print( life['animals'].keys())
print( life['animals']['cats'])
print('==================================================')

#-------------------8.10--------------------------#
squares = {x: x**2 for x in range(10)}
print(squares)

#-------------------8.11--------------------------#
odd = {i for i in range(10) if i % 2 == 1}
print(odd)
print('==================================================')

#-------------------8.12--------------------------#
#a_set = {: 'Got' for number in range(10)} ??????????????????????????????
#print(a_set)
#print('==================================================')
#Используйте включение генератора, чтобы вернуть строку 'Got ' и числа из
#диапазона range(10). Итерируйте по этой конструкции с помощью цикла for.

#-------------------8.13--------------------------#
keys = ('optimist', 'pessimist', 'troll')
values = ('The glass is half full','The glass is half empty', 'How did you get a glass?')
zipped = dict(zip(keys, values))
print(zipped)
print('==================================================')
#Используйте функцию zip(), чтобы создать словарь из кортежа ключей и кортежа значений

#-------------------8.14--------------------------#
titles = ['Creature of Habit', 'Crewel Fate', 'Sharks On a Plane']
plots = ['A nun turns into a monster', 'A haunted yarn shop', 'Check your exits']
movies = {movies for movies in zip(titles, plots)}
print(movies)
#Используйте функцию zip(), чтобы создать словарь с именем movies, в котором объединены списки titles и plots

