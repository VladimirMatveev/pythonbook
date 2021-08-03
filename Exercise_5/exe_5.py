song = """When an eel grabs your arm,
And it causes great harm,
That's - a moray!"""
print(song.replace('moray', 'Moray'))

#Q: вопрос
#A: ответ
questions = [
"We don't serve strings around here. Are you a string?",
"What is said on Father's Day in the forest?",
"What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
"An exploding sheep.",
"No, I'm a frayed knot.",
"'Pop!' goes the weasel."
]
print('1)',questions[0],'\n', answers[0])
print('2)',questions[1],'\n', answers[1])
print('3)',questions[2],'\n', answers[2])


#Выведите на экран следующее стихотворение, используя старый стиль форматирования.
#Подставьте в него такие строки: 'roast beef', 'ham', 'head' и 'clam':
sho1 = 'roast beef'
sho2 = 'ham'
sho3 = 'head'
sho4 = 'clam'

namea = '''My kitty cat likes %s,
My kitty cat likes %s,
My kitty cat fell on his %s
And now thinks he's a %s.''' % (sho1, sho2, sho3, sho4)
print(namea,'\n')

#Напишите письмо с использованием нового стиля форматирования. Сохраните
#предложенную строку в переменной letter (она понадобится вам в упражнении
#ниже):
salutation = 'Mr'
name = 'Siktir Byrdan'
product = 'shoe rack'
verbed = 'stood'
room = 'bedroom'
animals = 'dog'
amount = 'amount' #?
percent = '138'
spokesman = 'OOO Shoe Rack'
job_title = 'GOODJOB'
letter = '''Dear {salutation} {name},
Thank you for your letter. We are sorry that our {product}
{verbed} in your {room}. Please note that it should never
be used in a {room}, especially near any {animals}.
Send us your receipt and {amount} for shipping and handling.
We will send you another {product} that, in our tests,
is {percent}% less likely to have {verbed}.
Thank you for your support.
Sincerely,
{spokesman}
{job_title}'''.format(salutation='Mr', name='Siktir Byrdan', product='shoe rack', verbed='stood', room='bedroom',
                      animals='dog', amount='amount', percent='138', spokesman='OOO Shoe Rack', job_title='GOODJOB')
print(letter,'\n')

duck = 'McDuckFace'
pumpkin = 'McPumpkFace'
spitz = 'McSpitzface'
print('Вывод через % : ', '%s' % duck, pumpkin, spitz)
formaat = 'Вывод через format(), = {} , {} , {}'.format(duck, pumpkin, spitz)
print(formaat)
print(f'Вывод через f, = duck : {duck}, pumpkin : {pumpkin}, spitz : {spitz}')